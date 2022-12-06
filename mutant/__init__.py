from __future__ import unicode_literals

import logging

# from django.utils.version import get_version

VERSION = (0, 3, 0, 'alpha', 5)

__version__ = '.'.join([str(x) for x in VERSION])

logger = logging.getLogger('mutant')

default_app_config = 'mutant.apps.MutantConfig'
