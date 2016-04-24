# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import sys

from django.conf import settings
from getpass import getpass


def ensure_pragma_key():
    if not hasattr(settings, 'PRAGMA_KEY') or not settings.PRAGMA_KEY:
        sys.stderr.write("There is no SQL Cipher key defined, it's unsafe to store in your settings. Please input your key.\n\n")
        key = getpass("Key: ")
        settings.PRAGMA_KEY = key


class PromptForPragmaKeyMixin(object):
    """""
    This is a universal command that you can have other management commands
    inherit from in case they need database access.
    """

    def handle(self, *args, **options):
        ensure_pragma_key()
        super(PromptForPragmaKeyMixin, self).handle(*args, **options)
