from flask import Blueprint

bp_books = Blueprint('books', __name__)

@bp_books.route('/mostrar', methods=['GET'])

def mostrar():
  ...