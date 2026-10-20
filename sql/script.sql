-- script.sql
-- Crea la tabla "historial" si todavia no existe.
--
-- La tabla funciona como una PILA (LIFO: Last In, First Out):
-- "id" es autoincremental, asi que la pagina con el id MAS GRANDE
-- es la ultima que se visito (la "cima" de la pila).
--   - Apilar (visitar)   -> INSERT
--   - Desapilar (regresar) -> DELETE de la fila con el id mas grande
--   - Ver la cima (actual) -> SELECT ... ORDER BY id DESC LIMIT 1

CREATE TABLE IF NOT EXISTS historial (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL
);
