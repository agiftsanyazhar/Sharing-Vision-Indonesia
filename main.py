# main
from flask import Flask
from app.routes.article_route import article_bp
from app.routes.home_route import home_bp
from app.database import reset_database

reset_database()

app = Flask(__name__, template_folder="app/views", static_folder="app/static")
app.register_blueprint(article_bp)
app.register_blueprint(home_bp)

if __name__ == "__main__":
    app.run(debug=True)
