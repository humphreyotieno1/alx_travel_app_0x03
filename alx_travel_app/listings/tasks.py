from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

@shared_task(bind=True, max_retries=3)
def send_booking_confirmation_email(self, booking_id):
    """
    Task to send booking confirmation email asynchronously.
    
    Args:
        booking_id (UUID): The ID of the booking
    """
    from .models import Booking
    
    try:
        # Get the booking object
        booking = Booking.objects.select_related('user', 'property').get(id=booking_id)
        
        # Prepare email content
        subject = f'Booking Confirmation - {booking.property.name}'
        
        context = {
            'booking': booking,
            'property': booking.property,
            'user': booking.user,
            'start_date': booking.start_date.strftime('%B %d, %Y'),
            'end_date': booking.end_date.strftime('%B %d, %Y'),
            'total_price': booking.total_price,
        }
        
        # Render HTML email template
        html_message = render_to_string('emails/booking_confirmation.html', context)
        plain_message = strip_tags(html_message)
        
        # Send email
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[booking.user.email],
            html_message=html_message,
            fail_silently=False,
        )
        
        return f"Confirmation email sent for booking {booking_id}"
        
    except Exception as e:
        # Log the error and retry
        self.retry(exc=e, countdown=60 * 5)  # Retry after 5 minutes
        return f"Failed to send email for booking {booking_id}: {str(e)}"
