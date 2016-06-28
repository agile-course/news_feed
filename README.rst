News Feed
==============================

A reddit clone!

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


Settings
------------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html


Running tests locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~

$ python manage.py test

Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
$ gem update --system
$ gem install compass
$ compass compile --sass-dir news_feed/static/sass --css-dir news_feed/static/css

Local dev
^^^^^^
$ cd news_feed/static && bower install
$ pip install -r requirements/local.txt
$ python manage.py migrate
$ python manage.py runserver_plus
