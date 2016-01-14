#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import current_app as app
from path import Path


def get_memes(filter=None):
    """Get the memes from the filesystem."""
    if filter:
        return []
    else:
        d = Path(app.config['UPLOADS_DEFAULT_DEST'])
        return d.files()
