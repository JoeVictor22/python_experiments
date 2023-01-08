from app import celery as celery_app


@celery_app.task
def send_async_email( *args, **kwargs):
    """Background task to send an email with Flask-mail."""
    # with app.app_context():
    print("sending async mail")

    from pprint import pprint
    pprint(args)
    pprint(kwargs)
    try:
        pprint(self)
    except Exception:
        print("NO SELF REFERENCE")
@celery_app.task
def send_welcome_email():
    print("sending welcome mail")

