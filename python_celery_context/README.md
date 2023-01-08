# Description

# Commands

```shell
celery -A app.runcelery:celery beat



celery -A app:celery worker --loglevel=INFO --concurrency=2 -n worker1@%h


```

# Docker instructions

```shell
docker-compose up
```

# Code helps

```python

# generate n tasks
from app.tasks.workers import *
for i in range (10000):
    send_async_email.apply_async()
    send_welcome_email.apply_async()
```
