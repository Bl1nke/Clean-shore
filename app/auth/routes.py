
from flask import Blueprint, redirect, render_template, url_for


auth = Blueprint("auth", __name__)


@auth.get("/")
def index():
    """Use the sign-in screen as the application's entry point."""
    return redirect(url_for("auth.login"))


@auth.get("/login")
def login():
    """Render the role-selection sign-in screen."""
    return render_template("auth/login.html")
