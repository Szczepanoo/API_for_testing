from flask import Flask, render_template, request, jsonify, redirect, send_from_directory
import requests

app = Flask(__name__)

API_URL = "https://jsonplaceholder.typicode.com"

@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.ico')

@app.route('/static/style.css')
def css():
    return send_from_directory('static', 'style.css')

@app.route('/static/other_style.css')
def css_other_style():
    return send_from_directory('static', 'other_style.css')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def get_posts():
    response = requests.get(f"{API_URL}/posts")
    if response.status_code == 200:
        posts = response.json()
        return render_template('posts.html', posts=posts)
    else:
        return "Error fetching posts", 500


@app.route('/comments')
def get_comments():
    response = requests.get(f"{API_URL}/comments")
    if response.status_code == 200:
        comments = response.json()
        return render_template('comments.html', comments=comments)
    else:
        return "Error fetching comments", 500


@app.route('/albums')
def get_albums():
    response = requests.get(f"{API_URL}/albums")
    if response.status_code == 200:
        albums = response.json()
        return render_template('albums.html', albums=albums)
    else:
        return "Error fetching albums", 500


@app.route('/photos')
def get_photos():
    response = requests.get(f"{API_URL}/photos")
    if response.status_code == 200:
        photos = response.json()
        return render_template('photos.html', photos=photos)
    else:
        return "Error fetching photos", 500


@app.route('/set_display_limit', methods=['POST'])
def set_display_limit():
    limit = request.json.get('limit')
    # Code to set display limit
    return jsonify({'message': f'Display limit set to {limit}'}), 200


@app.route('/search_posts', methods=['POST'])
def search_posts():
    min_length = request.json.get('min_length')
    max_length = request.json.get('max_length')
    # Code to search posts by character length
    return jsonify({'message': f'Searching posts with character length between {min_length} and {max_length}'}), 200


@app.errorhandler(Exception)
def handle_error(error):
    app.logger.error(f'An error occurred: {error}')
    return 'An unexpected error occurred', 500


if __name__ == '__main__':
    app.run(debug=True)
