
from flask import Blueprint, request, jsonify
from sqlalchemy import or_

from app.libs.redprint import Redprint
from app.model.book import Book
from validators.forms import BookSearchForm

api = Redprint('book')


@api.route('/search')
def search():
    form = BookSearchForm().validate_for_api()
    q = f'%{form.q.data}%'
    books = Book.query.filter(or_(
        Book.title.like(q), Book.publisher.like(q)
    )).all()
    books = [book.hide('summary', 'id').append('pages') for book in books]
    return jsonify(books)


@api.route('/<int:isbn>/detail')
def detail(isbn):
    book = Book.query.filter_by(isbn=isbn).first_or_not_found()
    return jsonify(book)