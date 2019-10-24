from flask import Blueprint, jsonify, request

from . import db
from .models import Book

BookApi = Blueprint('book_api', __name__)


@BookApi.route('/create', methods=['POST'])
def create_book():

    try:
        book = Book.from_dict(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    db.session.add(book)
    db.session.commit()
    return jsonify(), 200


@BookApi.route('/<name>')
def get_book(name):
    book = Book.query.filter(Book.name == name).first()
    if book is None:
        return 'book not found', 404
    return jsonify(book.to_dict()), 200