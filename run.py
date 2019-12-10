from decouple import config
from flask_restful import Api

from app import create_app
from app.wish_app.controller import WishController

config_name = config('APPLICATION_SETTINGS', default='')
app = create_app(config_name)

services = Api(app, prefix='/api/v1')
services.add_resource(WishController, '/wishlist')

if __name__ == "__main__":
    app.run()
