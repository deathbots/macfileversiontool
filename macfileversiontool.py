# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

# import pytsk3
# import six
import platform

import sys

try:
    # Try pysqlite2 if it exists, as it could be statically linked/more modern
    from pysqlite2 import dbapi2 as sqlite
except ImportError:
    from sqlite3 import dbapi2 as sqlite


def print_stderr(*args, **kwargs):
    quit_me = kwargs.pop('bail', False)
    print(*args, file=sys.stderr, **kwargs)
    if quit_me:
        sys.exit(1)


if __name__ == '__main__':
    # todo: how to loop through and find the mounted dirs. Might need a flag for that.

    print('I live')
