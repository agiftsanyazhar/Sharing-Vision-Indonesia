# article_view
from flask import Blueprint
from app.controllers.article_controller import (
    save_post,
    get_post,
    get_posts,
    delete_post,
)

article_bp = Blueprint("article", __name__)

article_bp.route("/article/<int:limit>/<int:offset>", methods=["GET"])(get_posts)
article_bp.route("/article/<int:id>", methods=["GET"])(get_post)
article_bp.route("/article", methods=["POST"])(save_post)
article_bp.route("/article/<int:id>", methods=["POST"])(save_post)
article_bp.route("/article/<int:id>", methods=["DELETE"])(delete_post)
