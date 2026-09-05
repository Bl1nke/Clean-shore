

from flask import Blueprint, render_template


dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard.get("/")
def index():
    """Render the user's main workspace after sign-in."""
    return render_template("dashboard/index.html")
