from app import celery as celery_app


@celery_app.task
def send_async_email():
    """Background task to send an email with Flask-mail."""
    # with app.app_context():
    print("sending async mail")


@celery_app.task
def send_welcome_email():
    print("sending welcome mail")
