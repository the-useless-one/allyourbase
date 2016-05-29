#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = u'Yannick M\xe9heut'
SITENAME = u'All Your Base Are Belong To Me'
COPYRIGHT_YEAR = date.today().year
SITETITLE = SITENAME
SITESUBTITLE = u'You know, if that\'s alright with you'
SITEURL = 'https://allyourbase.utouch.fr'
SITELOGO = u'/images/useless_profile_pic.jpg'
CC_LICENSE = {'name': 'Creative Commons Attribution-ShareAlike', 'version': '4.0', 'slug': 'by-sa'}

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

FAVICON = u'/extras/favicon.ico'
CUSTOM_CSS = u'/extras/style.css'

MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),)

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAINE = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('envelope-o', 'mailto:yannick at meheut dot org'),
          ('github', 'https://github.com/the-useless-one/'),
          ('rss', 'https://allyourbase.utouch.fr/feeds/all.atom.xml'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'docs', 'extras']

THEME = '/var/www/allyourbase/pelican-themes/Flex'

PLUGIN_PATHS = ['/var/www/allyourbase/pelican-plugins']
PLUGINS = ['summary']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
