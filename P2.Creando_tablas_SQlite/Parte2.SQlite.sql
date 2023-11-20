CREATE TABLE stock (
    stock_id INTEGER PRIMARY KEY,
    sucursal_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    CONSTRAINT fk_sucursal FOREIGN KEY (sucursal_id) REFERENCES sucursal(sucursal_id),
    CONSTRAINT fk_producto FOREIGN KEY (producto_id) REFERENCES producto(producto_id),
    UNIQUE (sucursal_id, producto_id)
);

