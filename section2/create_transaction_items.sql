CREATE TABLE transaction_items (
    transaction_id int NOT NULL,
    item_id int NOT NULL,
    membership_id varchar(50) NOT NULL,
    item_quantity int NOT NULL,
    transaction_item_price NUMERIC(10,2) NOT NULL,
    transaction_item_weight NUMERIC(10,2) NOT NULL,
    subtotal_price NUMERIC(10,2) NOT NULL,
    subtotal_weight NUMERIC(10,2) NOT NULL,
    PRIMARY KEY (transaction_id, item_id)
);