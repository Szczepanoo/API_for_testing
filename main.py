"""
Ten moduł zawiera funkcje do obsługi aplikacji Flask
"""


from flask import (Flask, render_template, request, jsonify,
                   redirect, send_from_directory)
import requests

app = Flask(__name__)

API_URL = "https://jsonplaceholder.typicode.com"


@app.route('/favicon.ico')
def favicon():
    """
    Funkcja zwraca favicon
        :return: redirect()
    """
    return redirect('/static/favicon.ico')


@app.route('/static/style.css')
def css():
    """
    Funkcja zwraca style.css
        :return: send_from_directory()
    """
    return send_from_directory('static', 'style.css')


@app.route('/static/other_style.css')
def css_other_style():
    """
        Funkcja zwraca other_style.css
            :return: send_from_directory()
    """
    return send_from_directory('static', 'other_style.css')


@app.route('/')
def index():
    """
    Funkcja zwraca index.html
        :return: render_template()
    """
    return render_template('index.html')


@app.route('/posts')
def get_posts():
    """
        Funkcja zwraca posty z API
            :return: render_template()
    """
    response = requests.get(f"{API_URL}/posts", timeout=10)
    if response.status_code == 200:
        posts = response.json()
        return render_template('posts.html', posts=posts)
    return "Error fetching posts", 500


@app.route('/comments')
def get_comments():
    """
     Funkcja zwraca komentarze z API
                :return: render_template()
    """
    response = requests.get(f"{API_URL}/comments", timeout=10)
    if response.status_code == 200:
        comments = response.json()
        return render_template('comments.html', comments=comments)
    return "Error fetching comments", 500


@app.route('/albums')
def get_albums():
    """
         Funkcja zwraca albumy z API
                    :return: render_template()
        """
    response = requests.get(f"{API_URL}/albums", timeout=10)
    if response.status_code == 200:
        albums = response.json()
        return render_template('albums.html', albums=albums)
    return "Error fetching albums", 500


@app.route('/photos')
def get_photos():
    """
         Funkcja zwraca zdjęcia z API
                    :return: render_template()
        """
    response = requests.get(f"{API_URL}/photos", timeout=10)
    if response.status_code == 200:
        photos = response.json()
        return render_template('photos.html', photos=photos)
    return "Error fetching photos", 500


@app.route('/set_display_limit', methods=['POST'])
def set_display_limit():
    """
         Funkcja ustawia display limit
                    :return: jsonify()
        """
    limit = request.json.get('limit')
    # Code to set display limit
    return jsonify({'message': f'Display limit set to {limit}'}), 200


@app.route('/search_posts', methods=['POST'])
def search_posts():
    """
         Funkcja filtruje posty
                    :return: jsonify()
        """
    min_length = request.json.get('min_length')
    max_length = request.json.get('max_length')
    # Code to search posts by character length
    return jsonify({'message': f'Searching posts with character length '
                               f'between {min_length} and {max_length}'}), 200


@app.errorhandler(Exception)
def handle_error(error):
    """
         Funkcja zwraca bład, który wystąpił
                    :param: error
                    :return: app.logger.error()
        """
    app.logger.error('An error occurred: %s', error)
    return 'An unexpected error occurred', 500


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
