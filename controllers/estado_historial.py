"""
estado_historial.py
Opcion 5 (parte 1): verificar si el historial esta vacio (GET /estado).
Desde esta pantalla tambien se puede eliminar el historial.
"""

import web
from controllers.conexion import obtener_conexion
from controllers.utilidades import render, contar_paginas


class EstadoHistorial:
    def GET(self):
        datos = web.input(mensaje='')
        conexion = obtener_conexion()
        total = contar_paginas(conexion)
        conexion.close()
        return render.estado(total, datos.mensaje)
