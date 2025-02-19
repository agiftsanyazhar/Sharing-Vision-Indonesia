# home_route
from flask import Blueprint, render_template

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def all_posts():
    return render_template("articles/all-posts.html")
