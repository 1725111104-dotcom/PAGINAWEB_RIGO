"""
pagina_actual.py
Opcion 3: mostrar la pagina actual (GET /actual).
Es la cima de la pila; NO se saca de la pila, solo se consulta.
"""

from controllers.conexion import obtener_conexion
from controllers.utilidades import render, obtener_cima


class PaginaActual:
    def GET(self):
        conexion = obtener_conexion()
        actual = obtener_cima(conexion)
        conexion.close()
        return render.actual(actual)
