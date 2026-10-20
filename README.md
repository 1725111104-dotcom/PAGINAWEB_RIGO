# Simulador de navegador web (pila LIFO)

Aplicación web básica en **Python (web.py) + SQLite**, con arquitectura
**MVC**, que simula el historial de un navegador usando una **pila**:
la última página visitada es la primera en recuperarse (**LIFO**).

## Menú del programa

1. Visitar una página web
2. Regresar a la página anterior
3. Mostrar la página actual
4. Mostrar el historial en orden descendente (desde la página actual)
5. Verificar si el historial está vacío o eliminarlo
6. Salir del programa

## Estructura del proyecto

```
navegador-pila/
├── README.md
├── app.py                        # rutas -> controladores
├── requirements.txt
├── controllers/
│   ├── __init__.py
│   ├── conexion.py               # abre la conexión a sql/historial.db
│   ├── utilidades.py             # render, crear BD, redirigir, cima y conteo
│   ├── index.py                  # GET  /           -> menú principal
│   ├── visitar_pagina.py         # POST /visitar    -> apilar
│   ├── regresar_pagina.py        # POST /regresar   -> desapilar
│   ├── pagina_actual.py          # GET  /actual     -> ver la cima
│   ├── historial.py              # GET  /historial  -> recorrer de cima a base
│   ├── estado_historial.py       # GET  /estado     -> ¿vacío?
│   ├── borrar_historial.py       # POST /borrar     -> vaciar la pila
│   └── salir.py                  # GET  /salir
├── sql/
│   └── script.sql                # CREATE TABLE (historial.db se crea sola)
└── views/
    ├── layout.html
    ├── index.html
    ├── actual.html
    ├── historial.html
    ├── estado.html
    └── salir.html
```

## ¿Cómo funciona la pila?

La tabla `historial` tiene un `id` autoincremental, así que la página con
el `id` **más grande** es la última visitada (la **cima** de la pila):

| Operación de pila | Opción del menú | Consulta SQL |
|---|---|---|
| Apilar (push) | Visitar una página | `INSERT INTO historial (url) VALUES (?)` |
| Desapilar (pop) | Regresar | `DELETE FROM historial WHERE id = (SELECT MAX(id) FROM historial)` |
| Ver la cima (peek) | Página actual | `SELECT url FROM historial ORDER BY id DESC LIMIT 1` |
| Recorrer de cima a base | Historial descendente | `SELECT url FROM historial ORDER BY id DESC` |
| ¿Está vacía? | Verificar historial | `SELECT COUNT(*) FROM historial` (0 = vacía) |
| Vaciar la pila | Eliminar historial | `DELETE FROM historial` |

**Regresar** quita la página actual (la cima), así que la que estaba
debajo pasa a ser la actual. Solo se puede regresar si hay al menos 2
páginas en el historial.

## Cómo ejecutarlo

Necesitas Python 3. Desde la carpeta del proyecto:

```
python3 -m venv venv
source venv/bin/activate        # en Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 app.py
```

Abre en tu navegador: `http://localhost:8080`

Si quieres otro puerto: `python3 app.py 5000`.

La primera vez, `sql/historial.db` se crea automáticamente usando
`sql/script.sql`.

## Cómo subirlo a GitHub

```
git init
git add .
git commit -m "Simulador de navegador web con pila LIFO (MVC)"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/NOMBRE-DEL-REPO.git
git push -u origin main
```
