# Background Task Management with Celery and Email Notifications

This document explains how to set up and use Celery with RabbitMQ for handling background tasks and email notifications in the ALX Travel App.

## Prerequisites

1. Python 3.8+
2. RabbitMQ server
3. Redis (optional, for result backend)

## Installation

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Install RabbitMQ:
   - **Ubuntu/Debian**:
     ```bash
     sudo apt-get update
     sudo apt-get install -y rabbitmq-server
     sudo systemctl enable rabbitmq-server
     sudo systemctl start rabbitmq-server
     ```
   - **macOS (using Homebrew)**:
     ```bash
     brew install rabbitmq
     brew services start rabbitmq
     ```
   - **Windows**:
     Download and install from [RabbitMQ Downloads](https://www.rabbitmq.com/download.html)

## Configuration

1. Update your `.env` file with the following variables:
   ```
   # Celery Configuration
   CELERY_BROKER_URL=amqp://guest:guest@localhost:5672//
   
   # Email Configuration (for production)
   EMAIL_HOST=smtp.your-email-provider.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@example.com
   EMAIL_HOST_PASSWORD=your-email-password
   DEFAULT_FROM_EMAIL=noreply@alxtravel.com
   ```

## Running Celery Workers

1. Start the Celery worker in a separate terminal:
   ```bash
   # In the project root directory
   celery -A alx_travel_app worker -l info
   ```

2. (Optional) Start Celery beat for scheduled tasks:
   ```bash
   celery -A alx_travel_app beat -l info
   ```

## Testing the Email Notification

1. Make sure the Celery worker is running.
2. Create a new booking through the API.
3. Check the Celery worker logs to see the email task being processed.
4. In development, the email will be printed to the console. In production, it will be sent to the user's email.

## Verifying the Setup

1. Check if RabbitMQ is running:
   ```bash
   sudo rabbitmqctl status
   ```

2. Check if Celery can connect to RabbitMQ:
   ```bash
   celery -A alx_travel_app inspect ping
   ```

## Troubleshooting

1. **Celery can't connect to RabbitMQ**:
   - Ensure RabbitMQ is running
   - Check the connection URL in settings
   - Verify the RabbitMQ credentials

2. **Emails not being sent**:
   - Check Celery worker logs for errors
   - Verify email settings in your environment variables
   - In development, check the console output for the email content

## Production Notes

1. Use a process manager like Supervisor or systemd to manage Celery workers.
2. Consider using Redis as a result backend for better performance.
3. Set up monitoring for Celery and RabbitMQ in production.
4. Configure proper logging and error handling for email tasks.
