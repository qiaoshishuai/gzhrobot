# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle  #引入Handle.py模块，这个模块在之后写。

urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()