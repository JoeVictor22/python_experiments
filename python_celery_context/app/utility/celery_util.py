def init_celery(app, celery):
    """Add flask app context to celery.Task"""
    TaskBase = celery.Task
    print("creating celery_app")

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                print("calling app_context")
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
