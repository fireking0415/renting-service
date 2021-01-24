from flask import Flask


def create_app():
    from . import models
    from project import services
    from project import routes
    app = Flask(__name__)
    routes.init_app(app)
    services.init_app(app)
    return app
