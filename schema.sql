CREATE TABLE IF NOT EXISTS products(
    input_link TEXT,
    product_name TEXT,
    price TEXT,
    update_at TEXT,
    PRIMARY KEY (input_link, price)
);