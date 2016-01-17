#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

from flask import current_app as app
from path import Path


def get_memes(filter=None):
    """Get the memes from the filesystem."""
    if filter:
        return []
    else:
        d = Path(app.config['UPLOADS_DEFAULT_DEST'])
        return complete_memes_tags(d.files())


def complete_memes_tags(data):
    res = []

    for item in data:
        filename = item.name
        ext = item.ext.lower()

        if ext in app.config['IMAGE_EXT']:
            res.append('<img src="/meme/{0}" alt="{0}">'.format(filename))
        elif ext in app.config['VIDEO_EXT']:
            res.append('<video src="/meme/{0}" autoplay loop controls>'
                       "C'est la PLS ! Votre navigateur ne semble pas supporter les vidéos intégrées.\n"
                       'Vous pouvez toujours <a href="/meme/{0}">la télécharger</a> '
                       'et la visionner avec votre lecteur vidéo préféré !'
                       '</video>'.format(filename))
        elif ext in app.config['AUDIO_EXT']:
            res.append('<audio src="/meme/{0}" controls>'
                       "C'est la PLS ! Votre navigateur ne semble pas supporter la balise <code>audio</code>.\n"
                       'Vous pouvez toujours <a href="/meme/{0}">la télécharger</a> '
                       'et la visionner avec votre lecteur vidéo préféré !'
                       '</audio>'.format(filename))

    return res
