# article controller
from flask import request, jsonify
from app.models.article import Post
from app.database import get_db
from app.schemas import PostSchema, validate_request


def save_post(id=None):
    db = next(get_db())
    data = request.get_json()

    validation = validate_request(data, PostSchema)

    if "error" in validation:
        return (
            jsonify(
                {"success": False, "message": "Validation failed.", "error": validation}
            ),
            400,
        )

    if id:
        post = db.query(Post).filter(Post.id == id).first()
        if not post:
            return (
                jsonify(
                    {
                        "success": False,
                        "message": "Post not found.",
                        "error": "Post not found.",
                    }
                ),
                404,
            )

        for key, value in validation.model_dump().items():
            setattr(post, key, value)

        message = "Article updated successfully."
    else:
        post = Post(**validation.model_dump())

        db.add(post)

        message = "Article created successfully."

    db.commit()
    db.refresh(post)

    return (
        jsonify({"success": True, "message": message, "post": post.to_dict()}),
        201 if not id else 200,
    )


def get_posts(limit, offset):
    db = next(get_db())
    posts = db.query(Post).offset(offset).limit(limit).all()

    return (
        jsonify(
            {
                "success": True,
                "message": "Get posts successfully.",
                "data": [post.to_dict() for post in posts],
            }
        ),
        200,
    )


def get_post(id):
    db = next(get_db())
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Post not found.",
                    "error": "Post not found.",
                }
            ),
            404,
        )

    return (
        jsonify(
            {
                "success": True,
                "message": "Get post successfully.",
                "data": post.to_dict(),
            }
        ),
        200,
    )


def delete_post(id):
    db = next(get_db())
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Post not found.",
                    "error": "Post not found.",
                }
            ),
            404,
        )

    db.delete(post)
    db.commit()

    return jsonify({"success": True, "message": "Article deleted successfully."}), 200
