"""
Script Name : app.py
Description : Entry point of the entire application
Author      : @tonybnya
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
