# main
from flask import Flask
from app.routes.article_route import article_bp
from app.routes.dashboard_route import dashboard_bp
from app.database import reset_database
from flask_cors import CORS

reset_database()

app = Flask(__name__, template_folder="app/views", static_folder="app/static")
CORS(app)

app.register_blueprint(article_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(debug=True)
