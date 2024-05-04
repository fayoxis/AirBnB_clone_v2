#!/usr/bin/python3
"""
this script to genereate to archive
execute: fab -f 1-pack_web_static.py
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    this will make an archive on web_static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
