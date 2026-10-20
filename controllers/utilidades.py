"""
utilidades.py
Funciones de apoyo usadas por varios controladores.
"""
 
import os
import urllib.parse
 
import web
 
from controllers.conexion import obtener_conexion, RUTA_BASE
 
# Motor de plantillas: busca en la carpeta views/ y envuelve cada
# pagina con views/layout.html
render = web.template.render(os.path.join(RUTA_BASE, 'views'), base='layout')
 
 
def inicializar_bd():
    """Crea la tabla 'historial' si todavia no existe (usa sql/script.sql)."""
    ruta_script = os.path.join(RUTA_BASE, 'sql', 'script.sql')
    conexion = obtener_conexion()
    with open(ruta_script, 'r', encoding='utf-8') as archivo:
        conexion.executescript(archivo.read())
    conexion.commit()
    conexion.close()
 
 
def redirigir(ruta, mensaje):
    """Redirige a una ruta mandando un mensaje para mostrarlo en pantalla."""
    destino = ruta + '?mensaje=' + urllib.parse.quote(mensaje)
    # Usamos una direccion RELATIVA (ej: /?mensaje=...) en lugar de web.seeother,
    # que arma una direccion completa con el Host de la peticion. Asi el navegador
    # siempre vuelve a la misma direccion que ya esta usando (localhost, Codespaces,
    # puerto reenviado, etc.).
    raise web.HTTPError('303 See Other', {'Location': destino})
 
 
def obtener_cima(conexion):
    """Devuelve la URL de la ultima pagina visitada (cima de la pila) o None."""
    fila = conexion.execute(
        'SELECT url FROM historial ORDER BY id DESC LIMIT 1;'
    ).fetchone()
    return fila['url'] if fila else None
 
 
def contar_paginas(conexion):
    """Devuelve cuantas paginas hay en el historial."""
    return conexion.execute('SELECT COUNT(*) AS total FROM historial;').fetchone()['total']