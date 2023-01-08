from random import random
from pprint import pprint
from app import celery as celery_app
import sys

from memory_profiler import profile


@celery_app.task(bind=True)
def send_async_email(self):
    teste_cache(self, "async")


@celery_app.task(bind=True)
def send_welcome_email(self):
    teste_cache(self, "welcome")


# @profile
def teste_cache(task, type):
    print(f"sending {type} mail")
    wrong_type = "async" if type == "welcome" else "welcome"

    # self._cache["task_id"] = self.id
    task._cache_task["last_task_ran"] = type
    task._cache_task["runs"] += 1
    task._cache_task[type] += 1
    task._cache_task["runs"] += 1
    task._cache_task[type] += 1
    task._cache_task["runs"] += 1
    task._cache_task[type] += 1
    task._cache_task["blob"].append(random())

    if task._cache_task["runs"] != 3 or task._cache_task[wrong_type] > 0:
        pprint(task._cache_task)
        sys.exit(1)

    task._cache_worker["last_task_ran"] = type
    task._cache_worker["runs"] += 1
    task._cache_worker[type] += 1
    task._cache_worker["blob"].append(random())

    if (
        task._cache_worker["runs"] == 0
        or task._cache_worker[type] == 0
        or task._cache_worker["last_task_ran"] != type
    ):
        pprint(task._cache_worker)
        sys.exit(1)

    print(len(task._cache_task["blob"]))
    print(len(task._cache_worker["blob"]))

    print(sys.getsizeof(task._cache_task))
    print(sys.getsizeof(task._cache_worker))
