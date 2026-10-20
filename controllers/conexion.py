"""
conexion.py
Solo abre la conexion a la base de datos SQLite (sql/historial.db).
Todos los controladores usan esta funcion.
"""

import os
import sqlite3

# Ruta absoluta del proyecto, sin importar desde donde se ejecute
RUTA_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_BD = os.path.join(RUTA_BASE, 'sql', 'historial.db')


def obtener_conexion():
    conexion = sqlite3.connect(RUTA_BD)
    # Permite leer columnas por nombre, ej: fila['url']
    conexion.row_factory = sqlite3.Row
    return conexion
