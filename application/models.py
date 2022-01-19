''' Database entry models.'''

from . import db


class WishItem(db.Model):
    ''' Stores a single item entry. '''
    __tablename__ = 'wishlist'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        index=True,
        unique=True,
        nullable=False
    )
    price = db.Column(
        db.Float(asdecimal=True),
        index=False,
        unique=False,
        nullable=False
    )
    link = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )
    note = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def update(self, **data):
        self.name = data.get('name') or self.name
        self.price = data.get('price') or self.price
        self.link = data.get('link') or self.link
        self.note = data.get('note') or self.note
        return self.create()

    def delete(self):
        if self.id is not None:
            db.session.delete(self)
            db.session.commit()

    def __repr__(self):
        return '<WishItem {}>'.format(self.name)
