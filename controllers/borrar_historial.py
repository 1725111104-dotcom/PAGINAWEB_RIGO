"""
borrar_historial.py
Opcion 5 (parte 2): eliminar todo el historial (POST /borrar).
Deja la pila vacia.
"""

from controllers.conexion import obtener_conexion
from controllers.utilidades import redirigir, contar_paginas


class BorrarHistorial:
    def POST(self):
        conexion = obtener_conexion()

        if contar_paginas(conexion) == 0:
            conexion.close()
            redirigir('/estado', 'El historial ya estaba vacio, no hay nada que eliminar.')

        conexion.execute('DELETE FROM historial;')
        conexion.commit()
        conexion.close()

        redirigir('/estado', 'Historial eliminado correctamente.')
