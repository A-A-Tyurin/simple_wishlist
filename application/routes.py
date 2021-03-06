''' API endpoints. '''

from http import HTTPStatus

from flask import request, jsonify, make_response
from flask import current_app as app
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from .models import WishItem
from .schemas import WishItemSchema


@app.route('/', methods=['GET', 'POST'])
def wishlist():
    if request.method == 'POST':
        # Save new wishitem.
        try:
            item = WishItemSchema.parse_raw(request.data)
            db_new_item = WishItem(**item.dict()).create()
            response = WishItemSchema.from_orm(db_new_item).dict()
            status = HTTPStatus.CREATED
        except (ValidationError, IntegrityError) as error:
            response = str(error)
            status = HTTPStatus.BAD_REQUEST
    else:
        # Get list of wishitems.
        db_items = WishItem.query.all()
        response = [
            WishItemSchema.from_orm(db_item).dict() for db_item in db_items
        ]
        status = HTTPStatus.OK       
    return make_response(jsonify(response), status)


@app.route('/<id>', methods = ['GET', 'DELETE', 'PUT'])
def wishitem(id):
    db_item = WishItem.query.get(id)
    if db_item is None:
        return make_response(
            jsonify(HTTPStatus.NOT_FOUND.phrase), HTTPStatus.NOT_FOUND
        )

    if request.method == 'DELETE':
        # Delete wishitem by id.
        db_item.delete()
        response = ''
        status = HTTPStatus.NO_CONTENT
    elif request.method == 'PUT':
        # Full update wishitem by id.
        try:
            item = WishItemSchema.parse_raw(request.data)
            updated_item = db_item.update(**item.dict())
            response = WishItemSchema.from_orm(updated_item).dict()
            status = HTTPStatus.OK
        except ValidationError as error:
            response = str(error)
            status = HTTPStatus.BAD_REQUEST
    else:
        # Get wishitem by id.
        response = WishItemSchema.from_orm(db_item).dict()
        status = HTTPStatus.OK
    return make_response(jsonify(response), status)
