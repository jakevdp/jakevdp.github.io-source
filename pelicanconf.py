#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jake VanderPlas'
SITENAME = 'Pythonic Perambulations'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = ['ipynb.markup', 'summary']
IGNORE_FILES = ['.ipynb_checkpoints']

# THEME SETTINGS
THEME = './theme/'

DEFAULT_HEADER_BG = '/images/station1.jpg'
ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = 'jakevdp'
GITHUB_USERNAME = 'jakevdp'
SHOW_ARCHIVES = True
SHOW_FEED = True
