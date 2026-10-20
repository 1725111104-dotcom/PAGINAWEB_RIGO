"""
app.py
Punto de entrada de la aplicacion (web.py).
Conecta cada ruta (URL) con su controlador (clase).
"""

import web

from controllers.utilidades import inicializar_bd
from controllers.index import Index
from controllers.visitar_pagina import VisitarPagina
from controllers.regresar_pagina import RegresarPagina
from controllers.pagina_actual import PaginaActual
from controllers.historial import Historial
from controllers.estado_historial import EstadoHistorial
from controllers.borrar_historial import BorrarHistorial
from controllers.salir import Salir

# Ruta  ->  Clase controladora
urls = (
    '/',          'Index',
    '/visitar',   'VisitarPagina',
    '/regresar',  'RegresarPagina',
    '/actual',    'PaginaActual',
    '/historial', 'Historial',
    '/estado',    'EstadoHistorial',
    '/borrar',    'BorrarHistorial',
    '/salir',     'Salir',
)

# Nos aseguramos de que sql/historial.db y la tabla existan
inicializar_bd()

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
