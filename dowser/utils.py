#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: utils.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-11-24
"""
from contextlib import contextmanager
import cherrypy

from dowser import Root


@contextmanager
def server(port=8888, show_trace=True):

    try:
        config = {
            'environment': 'embedded',
            'server.socket_port': port,
        }
        if show_trace:
            config.update({
                'global': {
                    'request.show_tracebacks': True
                }}
            )
        cherrypy.tree.mount(Root())
        cherrypy.config.update(config)
        cherrypy.server.socket_port = port
        cherrypy.engine.start()
        yield cherrypy.engine
    finally:
        cherrypy.engine.exit()