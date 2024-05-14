"""
Ten moduł zawiera funkcje do obsługi aplikacji Flask
"""


import logging
from flask import (Flask, render_template, request,
                   jsonify, redirect, send_from_directory)
import requests
from requests.exceptions import HTTPError, Timeout
from sqlalchemy.exc import DatabaseError
import pstats
# import cProfile

app = Flask(__name__)

# Konfiguracja logowania
logging.basicConfig(filename='errors.log', level=logging.ERROR)

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
    Funkcja ustawia limit wyświetlanych elementów
    :return: jsonify()
    """
    limit = request.json.get('limit')
    if limit is not None and isinstance(limit, int) and limit > 0:
        # Tutaj możesz dodać kod do ustawienia limitu wyświetlanych elementów
        return jsonify({'message': f'Display limit set to {limit}'}), 200
    else:
        return jsonify({'error': 'Invalid display limit'}), 400


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


"""
    Logowanie błędów
"""


@app.errorhandler(HTTPError)
def handle_http_error(error):
    """
    Obsługa błędów HTTP
    """
    app.logger.error('HTTP error occurred: %s', error)
    return 'An unexpected HTTP error occurred', 500


@app.errorhandler(Timeout)
def handle_timeout_error(error):
    """
    Obsługa błędów timeout
    """
    app.logger.error('Timeout error occurred: %s', error)
    return 'An unexpected timeout error occurred', 500


@app.errorhandler(DatabaseError)
def handle_database_error(error):
    """
    Obsługa błędów bazy danych
    """
    app.logger.error('Database error occurred: %s', error)
    return 'An unexpected database error occurred', 500


@app.errorhandler(Exception)
def handle_error(error):
    """
    Funkcja obsługuje pozostałe błędy i loguje je do pliku dziennika
    :param error: Wyjątek lub błąd
    :return: Wiadomość błędu i status HTTP 500
    """
    app.logger.error('An error occurred: %s', error)
    return 'An unexpected error occurred', 500


def analyze_io_blocking_functions(profile_stats_file):
    """
    Analizuje wynik profilowania i identyfikuje funkcje blokujące IO.

    :param profile_stats_file: Ścieżka do pliku ze statystykami
    profilowania (wygenerowanego przez cProfile).
    """
    # Wczytaj statystyki profilowania
    stats = pstats.Stats(profile_stats_file)

    # Sortuj statystyki według łącznego czasu wywołań (cumtime)
    stats.sort_stats('cumulative')

    # Wydrukuj listę funkcji, które wywołują funkcje blokujące IO
    print("Funkcje blokujące IO:")
    for func, (_, file_name, line_number, _, _) in stats.stats.items():
        # Sprawdź, czy funkcja zawiera wywołania do metod
        # związanych z operacjami sieciowymi
        if 'requests.get' in func:
            print(f"Function: {func}, File: {file_name}, Line: {line_number}")


if __name__ == '__main__':
    # print("Aplikacja uruchomiona. Przejdź do:", "http://127.0.0.1:5000/")
    # # app.run(debug=True, use_reloader=False)
    # cProfile.run('app.run(debug=True, use_reloader=False)',
    # filename="app_profile_stats")

    # Ścieżka do pliku ze statystykami profilowania
    # profile_stats_file = 'app_profile_stats'
    # analyze_io_blocking_functions(profile_stats_file)

    p = pstats.Stats('app_profile_stats')
    p.strip_dirs().sort_stats(-1).print_stats()
