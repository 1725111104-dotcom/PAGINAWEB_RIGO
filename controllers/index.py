"""
index.py
Menu principal (GET /).
"""

import web
from controllers.utilidades import render


class Index:
    def GET(self):
        datos = web.input(mensaje='')
        return render.index(datos.mensaje)
