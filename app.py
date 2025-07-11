"""
Script Name : app.py
Description : Entry point of the entire application
Author      : @tonybnya
"""

from flask import Flask, render_template, request
from utils import get_artist_bio, get_artist_events, search_artist_or_event

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    results = search_artist_or_event(keyword)
    return render_template('search_results.html', results=results, keyword=keyword)


@app.route('/artist/<artist_id>')
def artist(artist_id):
    bio = get_artist_bio(artist_id)
    events = get_artist_events(artist_id)
    return render_template('artist.html', bio=bio, events=events)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
