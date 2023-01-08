from celery import Task

# -*- coding: utf-8 -*-
"""
Configure Celery. See the configuration guide at ->
http://docs.celeryproject.org/en/master/userguide/configuration.html#configuration
"""

## Broker settings.
broker_url = "pyamqp://guest:guest@localhost:5672//"
broker_heartbeat = 0

# List of modules to import when the Celery worker starts.
imports = ("app.tasks.workers",)

## Using the database to store task state and results.
result_backend = "rpc"
# result_persistent = False

accept_content = ["json", "application/text"]

result_serializer = "json"
timezone = "UTC"

# define periodic tasks / cron here
# beat_schedule = {
#    'add-every-10-seconds': {
#        'task': 'workers.add_together',
#        'schedule': 10.0,
#        'args': (16, 16)
#    },
# }

class TaskWithContext(Task):
    _cache_task = { # set to none or empty
        "runs": 0,
        "last_task_ran": "none",
        "welcome": 0,
        "async": 0
    }
    @staticmethod
    def inicializar_cache():
        return {
            "runs": 0,
            "last_task_ran": "none",
            "welcome": 0,
            "async": 0
        }
    def __init__(self, *args, **kwargs):
        super(TaskWithContext, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        self._cache_task = self.inicializar_cache()

        print("RESTART CACHE?")
        return super().__call__(*args, **kwargs)
    def apply_async(
        self,
        args=None,
        kwargs=None,
    ):
        return super().apply_async(
            args=args,
            kwargs=kwargs,
        )