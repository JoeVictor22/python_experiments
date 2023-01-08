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
