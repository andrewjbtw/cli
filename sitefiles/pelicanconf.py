#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andrew Berger'
SITENAME = u'notes on using the command line'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

MENUITEMS_MIDDLE = ( ('introduction', '/'), ('archives', '/archives.html'), ('contact', '/contact.html'), )

#DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
THEME = '../themes/pelican-octopress-theme'

#PAGE_PATHS = ['commands']
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']
#DIRECT_TEMPLATES = ['index', 'archives']

ARCHIVES_SAVE_AS = 'archives.html'

#MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}'

#PAGE_URL = 'command/{slug}/'
#PAGE_SAVE_AS = 'command/{slug}/index.html'


SUMMARY_MAX_LENGTH = None

DEFAULT_PAGINATION = 8
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
