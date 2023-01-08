from flask import Flask
from app import celery
from app.utility.celery_util import init_celery


def create_app(config):
    """
    Flask app factory
    """
    print("creating flask_app")
    app = Flask("app")
    app.config.from_object(config)
    init_celery(app, celery=celery)
    app.register_extensions()
    app.register_blueprints()
    app.register_errorhandlers()
    app.register_app_context_processors()
    return app
