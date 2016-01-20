#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

from flask import Flask, render_template, send_from_directory, abort
from flask.ext.uploads import UploadSet, ALL, configure_uploads, patch_request_class
from werkzeug import secure_filename

from memes import get_memes

# Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')

# Flask-Uploads
memes_up = UploadSet('memes', ALL)
configure_uploads(app, memes_up)
patch_request_class(app, app.config['MAX_CONTENT_LENGTH'])


@app.route('/')
@app.route('/<filter>')
def index(filter=None):
    """Hall of memes"""

    if filter not in [None, 'audio', 'video']:
        abort(404)
    return render_template('index.html', memes=get_memes(filter))


@app.route('/meme/<filename>')
def get_meme(filename):
    return send_from_directory(app.config['UPLOADS_DEFAULT_DEST'], secure_filename(filename))


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('img/favicon.ico')


@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')


# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="T'es en PLS ? Meme not found."), 404


@app.errorhandler(413)
def upload_too_big(e):
    error = ("Maximum upload size exceeded. T'as mis le serveur en PLS. "
             "You can't upload more than %s MB." % app.config['MAX_CONTENT_LENGTH'])
    return render_template('error.html', error=error), 413


# Template functions
def list_navbar():
    """Return the links for the navbar."""

    return [(name, url) for name, url in app.config['SITE_MENU']]
app.jinja_env.globals.update(list_navbar=list_navbar)

# Go!
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
