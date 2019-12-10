from decouple import config
from flask_restful import Api
from app.wish_app.controller import WishController
from app import create_app

config_name = config('APP_SETTINGS', default='')
app = create_app(config_name)

services = Api(app, prefix='/api/v1')
services.add_resource(WishController, '/wishlist')

if __name__ == "__main__":
    app.run()
