INSERT INTO customers (name, email, city, country)
VALUES
    ('Rahul Sharma', 'rahul@example.com', 'Dubai', 'UAE'),
    ('Ahmed Khan', 'ahmed@example.com', 'Abu Dhabi', 'UAE'),
    ('Sara Ali', 'sara@example.com', 'Sharjah', 'UAE'),
    ('John Mathew', 'john@example.com', 'Dubai', 'UAE'),
    ('Fatima Noor', 'fatima@example.com', 'Ajman', 'UAE'),
    ('Arjun Menon', 'arjun@example.com', 'Dubai', 'UAE'),
    ('Omar Hassan', 'omar@example.com', 'Abu Dhabi', 'UAE'),
    ('Priya Nair', 'priya@example.com', 'Sharjah', 'UAE'),
    ('Daniel Thomas', 'daniel@example.com', 'Dubai', 'UAE'),
    ('Aisha Rahman', 'aisha@example.com', 'Ras Al Khaimah', 'UAE');

    INSERT INTO products (name, category, price)
VALUES
    ('MacBook Air M3', 'Electronics', 1099.00),
    ('iPhone 16', 'Electronics', 899.00),
    ('Samsung Galaxy S25', 'Electronics', 799.00),
    ('Sony WH-1000XM5', 'Audio', 349.00),
    ('Apple AirPods Pro', 'Audio', 249.00),
    ('Logitech MX Master 3S', 'Accessories', 99.00),
    ('Keychron K8 Pro', 'Accessories', 129.00),
    ('Dell 27 Monitor', 'Monitors', 329.00),
    ('Anker USB-C Hub', 'Accessories', 59.00),
    ('Kindle Paperwhite', 'Electronics', 159.00),
    ('Nike Air Max', 'Footwear', 150.00),
    ('Adidas Ultraboost', 'Footwear', 180.00);

    INSERT INTO orders (customer_id, order_date, status)
VALUES
    (1, '2026-09-01 10:15:00', 'completed'),
    (2, '2026-09-02 14:30:00', 'completed'),
    (3, '2026-09-03 09:45:00', 'completed'),
    (4, '2026-09-05 16:20:00', 'pending'),
    (5, '2026-09-07 11:10:00', 'completed'),
    (6, '2026-09-09 13:50:00', 'cancelled'),
    (7, '2026-09-11 18:05:00', 'completed'),
    (8, '2026-09-13 12:25:00', 'completed'),
    (9, '2026-09-15 15:40:00', 'pending'),
    (10, '2026-09-17 10:05:00', 'completed'),
    (1, '2026-09-18 17:30:00', 'completed'),
    (2, '2026-09-20 09:20:00', 'completed'),
    (4, '2026-09-21 14:45:00', 'cancelled'),
    (6, '2026-09-23 11:55:00', 'completed'),
    (10, '2026-09-25 19:10:00', 'pending');


INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES
    (1, 1, 1, 1099.00),
    (1, 5, 2, 249.00),

    (2, 2, 1, 899.00),
    (2, 9, 1, 59.00),

    (3, 4, 1, 349.00),
    (3, 6, 2, 99.00),

    (4, 8, 1, 329.00),

    (5, 3, 1, 799.00),
    (5, 10, 2, 159.00),

    (6, 7, 1, 129.00),

    (7, 12, 2, 180.00),
    (7, 11, 1, 150.00),

    (8, 5, 1, 249.00),
    (8, 6, 1, 99.00),

    (9, 1, 1, 1099.00),

    (10, 10, 1, 159.00),
    (10, 9, 2, 59.00),

    (11, 2, 1, 899.00),
    (11, 4, 1, 349.00),

    (12, 3, 1, 799.00),

    (13, 8, 1, 329.00),

    (14, 1, 1, 1099.00),
    (14, 7, 1, 129.00),

    (15, 12, 1, 180.00),
    (15, 5, 1, 249.00);


    INSERT INTO payments (order_id, amount, payment_date, payment_method, status)
VALUES
    (1, 1597.00, '2026-09-01 10:20:00', 'card', 'completed'),
    (2, 958.00, '2026-09-02 14:35:00', 'card', 'completed'),
    (3, 547.00, '2026-09-03 09:50:00', 'card', 'completed'),
    (4, 329.00, '2026-09-05 16:25:00', 'card', 'pending'),
    (5, 1117.00, '2026-09-07 11:15:00', 'bank_transfer', 'completed'),
    (6, 129.00, '2026-09-09 13:55:00', 'card', 'failed'),
    (7, 510.00, '2026-09-11 18:10:00', 'card', 'completed'),
    (8, 348.00, '2026-09-13 12:30:00', 'cash', 'completed'),
    (9, 1099.00, '2026-09-15 15:45:00', 'card', 'pending'),
    (10, 277.00, '2026-09-17 10:10:00', 'card', 'completed'),
    (11, 1248.00, '2026-09-18 17:35:00', 'card', 'completed'),
    (12, 799.00, '2026-09-20 09:25:00', 'bank_transfer', 'completed'),
    (13, 329.00, '2026-09-21 14:50:00', 'card', 'failed'),
    (14, 1228.00, '2026-09-23 12:00:00', 'card', 'completed'),
    (15, 429.00, '2026-09-25 19:15:00', 'cash', 'pending');