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
    if platform.system() != 'Darwin':
        print_stderr('This must be run on a MacOS system', bail=True)
    mac_ver = platform.mac_ver()[0]
    print('Mac version {}'.format(mac_ver))
    mac_minor = mac_ver.split('.')[1]
    print('Mac minor version is {}'.format(mac_minor))
    if int(mac_minor) < 7:
        print_stderr('MacOS < version 10.7, there are no local file versions available.', bail=True)
    print('I live')
