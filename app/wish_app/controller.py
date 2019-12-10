from flask import jsonify
from flask_restful import Resource

from app.wish_app.services import WishServices


class WishController(Resource):

    def get(self):
        result = WishServices.get_all()
        response = jsonify(result)
        response.status_code = 200
        return response
