DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    first_scrape TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    first_price TEXT NOT NULL
);