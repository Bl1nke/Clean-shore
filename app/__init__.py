<<<<<<< HEAD
"""Application factory for the Clean Shore web service."""

from flask import Flask


def create_app() -> Flask:
    """Create and configure the application."""
    app = Flask(__name__)

    from app.auth.routes import auth
    from app.dashboard.routes import dashboard

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
=======
"""Application package for the Clean Shore web service."""
from flask import Flask
from app.map.routes import map_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(map_bp)
>>>>>>> 2bba3ac (Добавлена карта)
    return app
