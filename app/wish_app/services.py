from typing import List
from flask import jsonify
from app.wish_app.schema import WishSchema
from .models import WishModel


class WishServices:



    @staticmethod
    def get_all() -> List[WishModel]:
        query_result = WishModel.query.all()
        schema = WishSchema(many=True)
        result = schema.dump(query_result)
        return jsonify({'wish_list': result})


    @staticmethod
    def get_item_by_id(wish_id: int) -> WishModel:
        return WishModel.query.get(wish_id)
