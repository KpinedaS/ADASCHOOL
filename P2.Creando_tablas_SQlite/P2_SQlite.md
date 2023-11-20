Parte 2: Creando las tablas en SQLite
Dada la base de datos que diseñamos en la anterior etapa, escribe las consultas para crear cada una de las tablas en SQLite.

La tabla stock debe tener una restricción de unicidad unique (sucursal_id, producto_id).

Una restricción unique se utiliza de la siguiente forma:

CREATE TABLE someTable (
    id serial PRIMARY KEY,
    col1 int NOT NULL,
    col2 int NOT NULL,
    UNIQUE (col1, col2)
)