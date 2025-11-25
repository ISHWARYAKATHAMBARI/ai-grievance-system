from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from app.extensions import db, jwt
from app.config import Config

# Import blueprints
from app.api.auth import auth
from app.api.petitions import petitions
from app.api.departments import departments
from app.api.analytics import analytics
from app.api.notifications import notifications

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enable CORS
    CORS(app)

    # Init extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(petitions, url_prefix="/petitions")
    app.register_blueprint(departments, url_prefix="/departments")
    app.register_blueprint(analytics, url_prefix="/analytics")
    app.register_blueprint(notifications, url_prefix="/notifications")

    @app.route("/")
    def home():
        return {"status": "online", "message": "🔥 AI Grievance System API Ready!"}

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)




