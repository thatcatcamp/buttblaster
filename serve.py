# SPDX-License-Identifier: LGPL-3.0
"""
    this is a simple server - most linux distros are using snaps now, so browsers can't open
    fs items - this just serves /tmp on 8080 locally
"""

import cherrypy

PATH = "/tmp/"


class Root(object): pass


cherrypy.tree.mount(Root(), '/', config={
    '/': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': PATH,
        'tools.staticdir.index': 'index.html',
    },
})

cherrypy.quickstart()
