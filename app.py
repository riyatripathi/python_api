import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import sqlite3
import jwt
from datetime import datetime, timedelta
from jwt.exceptions import InvalidTokenError as JWTError

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE = os.getenv('DATABASE')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

def get_db():
    return sqlite3.connect(DATABASE)

@app.errorhandler(JWTError)
def handle_invalid_token(error):
    response = {
        'message': 'Invalid token',
        'error': str(error)
    }
    return jsonify(response), 401

# Login API
@app.route('/login', methods=['POST'])
def login():
    db = get_db()
    cursor = db.cursor()

    email = request.json['email']
    password = request.json['password']

    # Validate email existence in the database
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    if not user:
        return jsonify({'message': 'Invalid email or password'}), 401

    # Perform password validation (you may want to use a more secure method like hashing and salting)
    if user[2] != password:
        return jsonify({'message': 'Invalid email or password'}), 401

    # Generate a JWT token
    token = jwt.encode({
        'id': user[0],
        'exp' : datetime.utcnow() + timedelta(minutes = 30)
    }, app.config['SECRET_KEY'],algorithm="HS256")

    return jsonify({'token' : token}), 200

# List of Books API
@app.route('/books', methods=['GET'])
def get_books():
    token = None
    if 'Authorization' in request.headers:
        token = request.headers['Authorization'].split(' ')[1]
    if not token:
        return jsonify({'message' : 'Token is missing !!'}), 401


    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        user_id = data['id']
        print(user_id)
    except:
        return jsonify({
            'message' : 'Token is invalid !!',
            'token': token
        }), 401

    db = get_db()
    cursor = db.cursor()

    # Perform database query to fetch the list of books
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()

    book_list = []
    for book in books:
        book_dict = {
            'id': book[0],
            'title': book[1],
            'author': book[2]
        }
        book_list.append(book_dict)

    return jsonify({'books': book_list}), 200

if __name__ == '__main__':
    app.run(debug=True)