#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jake VanderPlas'
SITENAME = 'Pythonic Perambulations'
SITESUBTITLE = u'Musings and ramblings through the world of Python and beyond'
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

#MARKUP = ('md', 'ipynb')
#PLUGINS = ['ipynb.markup']

MARKUP = ['md']
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = ['summary', 'ipynb.liquid', # 'liquid_tags.notebook',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.literal']
IGNORE_FILES = ['.ipynb_checkpoints']

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# THEME SETTINGS
THEME = './theme/'

ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = 'jakevdp'
GITHUB_USERNAME = 'jakevdp'
STACKOVERFLOW_ADDRESS = 'http://stackoverflow.com/users/2937831/jakevdp'
SHOW_ARCHIVES = True
SHOW_FEED = True

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']

# Footer info

LICENSE_URL = "https://github.com/jakevdp/jakevdp.github.io-source/blob/master/LICENSE"
LICENSE = "MIT"
