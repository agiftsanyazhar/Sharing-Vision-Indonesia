# article_route
from flask import Blueprint
from app.controllers.article_controller import (
    save_post,
    all_posts,
    get_posts,
    get_post,
    delete_post,
)

article_bp = Blueprint("article", __name__)

article_bp.route("/api/article", methods=["GET"])(all_posts)
article_bp.route("/api/article/<int:limit>/<int:offset>", methods=["GET"])(get_posts)
article_bp.route("/api/article/<int:id>", methods=["GET"])(get_post)
article_bp.route("/api/article", methods=["POST"])(save_post)
article_bp.route("/api/article/<int:id>", methods=["POST"])(save_post)
article_bp.route("/api/article/<int:id>", methods=["DELETE"])(delete_post)
