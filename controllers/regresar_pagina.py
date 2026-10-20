"""
regresar_pagina.py
Opcion 2: regresar a la pagina anterior (POST /regresar).
DESAPILA la cima (la pagina actual); la que estaba debajo pasa a ser
la actual. Solo se puede regresar si hay al menos 2 paginas.
"""

from controllers.conexion import obtener_conexion
from controllers.utilidades import redirigir, obtener_cima, contar_paginas


class RegresarPagina:
    def POST(self):
        conexion = obtener_conexion()

        if contar_paginas(conexion) < 2:
            conexion.close()
            redirigir('/', 'No hay una pagina anterior a la cual regresar.')

        # Quitamos la cima de la pila (el id mas grande)
        conexion.execute(
            'DELETE FROM historial WHERE id = (SELECT MAX(id) FROM historial);'
        )
        conexion.commit()

        nueva_actual = obtener_cima(conexion)
        conexion.close()

        redirigir('/', 'Regresaste a: ' + nueva_actual)
