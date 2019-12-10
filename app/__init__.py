from flask_api import FlaskAPI
from settings.config import app_config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name: str) -> object:
    """Instanciate App from config"""
    app = FlaskAPI(__name__, settings_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODICFICATIONS'] = False
    db.init_app(app)

    return app