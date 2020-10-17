myDigitalDevops Cookiecutter
============================

.. image:: https://travis-ci.com/mydigitaldevops-com/mydigitaldevops-cookiecutter.svg?token=R8Tn11BhRZsxq7H1aJRF&branch=main
    :target: https://travis-ci.com/mydigitaldevops-com/mydigitaldevops-cookiecutter

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


Powered by Cookiecutter.
A sweet command-line tool that generates projects from templates for developing, shipping
and maintaining software with ease.

This Cookiecutter will provide the starting point to spinup a robust Development/Production Django-based environment.

Features
---------
*Builds, Tests and High coverage results for each generated projects.*

* Django 3.0, works with Python 3.8
* 12-Factor_ based settings with django-environ_
* Registration via django-allauth_
* Customizable PostgreSQL version
* Integration with MailHog_ for local email testing
* Twitter Bootstrap_ v4
* Default integration with pre-commit_ for identifying issues before pushing your repo... we love Quality ;)
* Running tests with unittest or pytest
* Environment variables for configuration (This won't work out of the box with Apache/mod_wsgi).

Optional Integrations
---------------------
*These features can be enabled during initial project setup.*

* Docker support using docker-compose_ for development and production (using Traefik_ with LetsEncrypt_ support)
* Configuration for Celery_ and Flower_ (Docker setup only)
* Send emails via Anymail_ (using Mailgun_ or Mailjet_)
* Serve static files from Amazon S3, Google Cloud Storage or Whitenoise_
* Basic ASGI setup for Websockets
* Custom static build using Gulp and livereload
* Deployment to Heroku (Procfile_)
* Integration with Sentry_ for error logging

.. _Bootstrap: https://github.com/twbs/bootstrap
.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _django-allauth: https://github.com/pennersr/django-allauth
.. _django-avatar: https://github.com/grantmcconnaughey/django-avatar
.. _Procfile: https://devcenter.heroku.com/articles/procfile
.. _Mailgun: http://www.mailgun.com/
.. _Whitenoise: https://whitenoise.readthedocs.io/
.. _Celery: http://www.celeryproject.org/
.. _Flower: https://github.com/mher/flower
.. _Anymail: https://github.com/anymail/django-anymail
.. _MailHog: https://github.com/mailhog/MailHog
.. _Sentry: https://sentry.io/welcome/
.. _docker-compose: https://github.com/docker/compose
.. _Traefik: https://traefik.io/
.. _LetsEncrypt: https://letsencrypt.org/
.. _pre-commit: https://github.com/pre-commit/pre-commit
.. _Mailjet: https://www.mailjet.com


Usage:
------
* `Developing locally`_
* `Developing locally using docker`_

.. _options:
.. _`Developing locally`:
.. _`Developing locally using docker`:

Community
-----------

* Have questions? please post your question on our `Google group`_. We check there periodically for questions.
* If you think you found a bug or want to request a feature, please open an issue_.
* For anything else, you can chat with us on `Slack`_.

.. _`Google group`:
.. _`issue`: https://github.com/mydigitaldevops-com/mydigitaldevops-cookiecutter/issues
.. _`Slack`: https://join.slack.com/


Credits
-------

This package was created with Cookiecutter_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter


Code of Conduct
---------------

Everyone interacting in our project's codebase, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.

.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/


License
-------

mydigitaldevops-cookiecutter package is licensed under the `GNU GPL v3`_.

.. _`GNU GPL v3`: https://www.gnu.org/licenses/gpl-3.0.en.html
