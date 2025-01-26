CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (name, email, password) VALUES
('alina', 'makaralina@gmail.com', 'malvina1234'),
('nick', 'nikitosik@gmail.com', 'nick0987654321');

