"""Application factory for the Clean Shore web service."""

from flask import Flask


def create_app() -> Flask:
    """Create and configure the application."""
    app = Flask(__name__)

    from app.auth.routes import auth

    app.register_blueprint(auth)
    return app
