"""
salir.py
Opcion 6: salir del programa (GET /salir).
"""

from controllers.utilidades import render


class Salir:
    def GET(self):
        return render.salir()
