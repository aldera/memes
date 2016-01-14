#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os

# app
DEBUG = True
SITE_NAME = 'Memes by Aldera #MST'
SITE_MENU = [('Audio', '/audio'),
             ('Video', '/video'),
             ('Gif', '/gif')]

# Flask-Uploads
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
if DEBUG:
    UPLOADS_DEFAULT_DEST = "D:\perso\memes"
else:
    UPLOADS_DEFAULT_DEST = os.path.join(APP_ROOT, 'uploads')
MAX_CONTENT_LENGTH = 25 * 1024 * 1024  # 25 MB
