from app import db


class WishModel(db.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'wish_model'

    id = db.Column(db.Integer, primary_key=True)
    wish_title = db.Column(db.String(200), index=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, wish_title):
        self.wish_title = wish_title

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<WishList: {}>".format(self.wish_title)