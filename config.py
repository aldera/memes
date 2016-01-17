#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import os

# app
DEBUG = True
SITE_NAME = 'Memes by Aldera #MST'
SITE_MENU = [('Audio', '/audio'),
             ('Video', '/video')]
VIDEO_EXT = ['.mp4', '.webm']
IMAGE_EXT = ['.jpg', '.jpe', '.jpeg', '.png', '.gif', '.svg', '.bmp']
AUDIO_EXT = ['.wav', '.mp3', '.aac', '.ogg', '.oga', '.flac']

# Flask-Uploads
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOADS_DEFAULT_DEST = os.path.join(APP_ROOT, 'uploads')
MAX_CONTENT_LENGTH = 25 * 1024 * 1024  # 25 MB
