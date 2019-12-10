from .models import WishModel
from app import ma


class WishSchema(ma.ModelSchema):
        class Meta:
            model = WishModel
