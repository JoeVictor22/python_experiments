from celery import Celery

celery = Celery("celery_app", config_source="app.celeryconfig", task_cls="app.celeryconfig.TaskWithContext")
