#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import Flask, render_template
from flask.ext.uploads import UploadSet, ALL, configure_uploads, patch_request_class

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
    return render_template('index.html', memes=get_memes(filter))


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('img/favicon.ico')


# Error handling
@app.errorhandler(403)
def forbidden_403(error):
    return render_template('403.html'), 403


@app.errorhandler(404)
def not_found_404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error_500(error):
    return render_template('500.html'), 500


# Template functions
def list_routes():
    """Return the links for the navbar."""
    return [(name, url) for name, url in app.config['SITE_MENU']]
app.jinja_env.globals.update(list_routes=list_routes)

# Go!
if __name__ == '__main__':
    app.run(host='0.0.0.0')
