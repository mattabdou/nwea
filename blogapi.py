from flask import Flask, jsonify, request, make_response
from flask_api import status
import json
import sqlite3
import os.path

app = Flask(__name__)

# Define custom error handler to return an API-friendly JSON response
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Function to return all blog posts in JSON array
@app.route('/posts')
def get_posts():

	# Get correct path to filesystem-based SQLite database
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(BASE_DIR, "blog.db")

	# Open connection and run query to get blog posts
	sqlconnection = sqlite3.connect(db_path)
	sqlconnection.row_factory = sqlite3.Row
	sqlcursor = sqlconnection.cursor()
	sqlcursor.execute('SELECT * FROM posts')
	all_posts = sqlcursor.fetchall()
	sqlconnection.commit()
	sqlconnection.close()

	# Return rows from query as JSON
	return json.dumps([dict(p) for p in all_posts]), status.HTTP_200_OK

# Function to save a new blog post and return new post_id
@app.route('/post', methods=['POST'])
def save_post():

	# Make sure input data is correct type
	if not request.json or not 'title' in request.json or not 'body' in request.json:
		return jsonify({'error':'Post must contain JSON with title and body key/value pairs'}), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

	# Get correct path to filesystem-based SQLite database
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(BASE_DIR, "blog.db")

	# Open connection and run query to save blog post
	sqlconnection = sqlite3.connect(db_path)
	sqlcursor = sqlconnection.cursor()
	sqlcursor.execute('''INSERT INTO posts(title, body)
						 VALUES(?,?)''',(request.json['title'], request.json['body']))
	sqlconnection.commit()
	newid = sqlcursor.lastrowid
	sqlconnection.close()

	# Return success with new post_id value
	return jsonify({'post_id': newid}), status.HTTP_201_CREATED