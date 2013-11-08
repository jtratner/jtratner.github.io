#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jeff Tratner'
SITENAME = u'Jeff Tratner'
SITEURL = 'http://www.jeffreytratner.com/blog'
THEME = './pelican-bootstrap3'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# get info from files
FILENAME_METADATA = "(?P<date>\d{4}-\d{2}-\d{2})?[_-](?P<slug>.*)"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# # Blogroll
LINKS =  (('My main page', 'http://jeffreytratner.com/'),)
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

GITHUB_URL = 'https://www.github.com/jtratner'
GITHUB_USER = 'jtratner'
# pelican-bootstrap3 options
GITHUB_SHOW_USER_LINK=True
GITHUB_REPO_COUNT=4
GITHUB_SKIP_FORK=False

BOOTSTRAP_THEME='cosmo'

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
