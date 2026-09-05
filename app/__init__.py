
from flask import Flask
from app.map.routes import map_bp


def create_app() -> Flask:
    """Create and configure the application."""
    app = Flask(__name__)

    from app.auth.routes import auth
    from app.dashboard.routes import dashboard
    from app.profile.routes import profile

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(map_bp)
    app.register_blueprint(profile)

    return app
