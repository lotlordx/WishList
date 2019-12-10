from typing import List
from .models import WishModel


class WishServices:

    @staticmethod
    def get_all() -> List[WishModel]:
        return WishModel.query.all()

    @staticmethod
    def get_item_by_id(widget_id: int) -> WishModel:
        return WishModel.query.get(widget_id)
