# main
from flask import Flask
from app.views.article_view import article_bp
from app.database import reset_database

reset_database()


app = Flask(__name__)
app.register_blueprint(article_bp)

if __name__ == "__main__":
    app.run(debug=True)
