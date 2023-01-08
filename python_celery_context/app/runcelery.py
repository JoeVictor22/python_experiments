from flask.helpers import get_debug_flag
from app import celery
from app.app import create_app
from app.utility.celery_util import init_celery

app = create_app({})
celery_app = init_celery(app, celery)
