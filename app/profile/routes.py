"""Profile page routes."""

from pathlib import Path

from flask import Blueprint, send_from_directory

PROFILE_DIR = Path(__file__).resolve().parent

profile = Blueprint("profile", __name__, url_prefix="/profile")


@profile.get("/")
def index():
    """Serve the existing personal cabinet page."""
    return send_from_directory(PROFILE_DIR, "profile.html")


@profile.get("/profile.css")
def stylesheet():
    """Serve styles that belong with the profile page."""
    return send_from_directory(PROFILE_DIR, "profile.css")
