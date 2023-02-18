CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    membership_id varchar(50) NOT NULL,
    total_items_price NUMERIC(10,2) NOT NULL,
    total_items_weight NUMERIC(10,2) NOT NULL
);