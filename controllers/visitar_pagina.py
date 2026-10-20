"""
visitar_pagina.py
Opcion 1: visitar una pagina web (POST /visitar).
APILA la pagina: se agrega al final, queda como la cima de la pila.
"""

import web
from controllers.conexion import obtener_conexion
from controllers.utilidades import redirigir


class VisitarPagina:
    def POST(self):
        datos = web.input(url='')
        url = datos.url.strip()

        if url == '':
            redirigir('/', 'Escribe la direccion de una pagina para visitarla.')

        conexion = obtener_conexion()
        conexion.execute('INSERT INTO historial (url) VALUES (?);', (url,))
        conexion.commit()
        conexion.close()

        redirigir('/', 'Visitaste: ' + url)
