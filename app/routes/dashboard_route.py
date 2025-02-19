# dashboard_route
from flask import Blueprint, render_template, request

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def all_posts():
    return render_template("articles/all-posts.html")


@dashboard_bp.route("/create-post")
def create_post():
    return render_template("articles/create-post.html")


@dashboard_bp.route("/edit-post/<int:id>")
def edit_post(id):
    return render_template("articles/edit-post.html", id=id)


@dashboard_bp.route("/preview")
def preview():
    return render_template("articles/preview.html")
