from .main import bp  # == from delivery.ext.site import bp


def init_app(app):
    app.register_blueprint(bp)