from .home_route import home


def init_app(app):
    app.register_blueprint(home)
    return None
