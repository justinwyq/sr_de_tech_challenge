CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name varchar(50) NOT NULL,
    manufacturer_name varchar(50) NOT NULL,
    item_cost NUMERIC(10,2) NOT NULL,
    item_weight NUMERIC(10,2) NOT NULL
);