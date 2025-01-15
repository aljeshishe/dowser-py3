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


def launch_memory_usage_server(port=8080, host='0.0.0.0', show_trace=False, show_log=False):
    config = {
        'environment': 'embedded',
        'server.socket_port': port,
        'server.socket_host': host,
    }


    if not show_log:
        cherrypy.log.error_log.propagate = False
        cherrypy.log.access_log.propagate = False


    if show_trace:
        config['global'] = {'request.show_tracebacks': True}
        
    cherrypy.tree.mount(Root())
    cherrypy.config.update(config)
    cherrypy.engine.start()
    return cherrypy.engine
        