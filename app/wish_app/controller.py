from flask import jsonify, request
from flask_restful import Resource

from app.wish_app.models import WishModel
from app.wish_app.services import WishServices


class WishController(Resource):

    def get(self):
        response = WishServices.get_all()
        response.status_code = 200
        return response

    def post(self):
        print("Hello World")
        name = str(request.data.get('name', None))
        if name:
            bucketlist = WishModel(wish_title=name)
            bucketlist.save()
            response = jsonify({
                'id': bucketlist.id,
                'name': bucketlist.wish_title,
                'date_created': bucketlist.created_at,
                'date_modified': bucketlist.updated_at
            })
            response.status_code = 201
            return response