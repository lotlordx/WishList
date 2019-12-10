from flask_api import FlaskAPI
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from settings.config import app_config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(config_name: str) -> object:
    """Instanciate App from config"""
    from app import app_loader

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)


    return app
