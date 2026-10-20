"""
historial.py
Opcion 4: mostrar el historial en orden descendente (GET /historial).
Empieza por la pagina actual (la ultima visitada) hasta la primera.
"""

from controllers.conexion import obtener_conexion
from controllers.utilidades import render


class Historial:
    def GET(self):
        conexion = obtener_conexion()
        filas = conexion.execute(
            'SELECT url FROM historial ORDER BY id DESC;'
        ).fetchall()
        conexion.close()

        paginas = [fila['url'] for fila in filas]
        return render.historial(paginas)
