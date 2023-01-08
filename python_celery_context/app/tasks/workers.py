from pprint import pprint
from app import celery as celery_app


@celery_app.task(bind=True)
def send_async_email(self):
    teste_cache(self, "async")

@celery_app.task(bind=True)
def send_welcome_email(self):
    teste_cache(self, "welcome")

def teste_cache(task, type):
    print(f"sending {type} mail")

    # self._cache["task_id"] = self.id
    task._cache_task["last_task_ran"] = type
    task._cache_task["runs"] += 1
    task._cache_task[type] += 1
    task._cache_task["runs"] += 1
    task._cache_task[type] += 1
    task._cache_task["runs"] += 1
    task._cache_task[type] += 1

    if task._cache_task["runs"] != 3 or task._cache_task["async" if type == "welcome" else "welcome"] > 0:
        pprint(task._cache_task)
        raise Exception()
