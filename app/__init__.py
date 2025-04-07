from flask import Flask
from .database import init_db
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["MONGO_URI"] = Config.MONGO_URI
    app.config["SECRET_KEY"] = Config.SECRET_KEY
    app.config["OPENAI_API_KEY"] = Config.OPENAI_API_KEY
    print("Mongo URI:", app.config["MONGO_URI"])
    init_db(app)

    #print("Mongo instance:", mongo.db)


    from .routes.auth import auth_bp
    from .routes.websites import website_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(website_bp, url_prefix="/api/websites")

    return app
