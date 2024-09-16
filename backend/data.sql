CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    -- images
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE socials (
    user_id INTEGER NOT NULL,
    facebook TEXT,
    twitter TEXT,
    linedin TEXT,
    pintrest TEXT,
    instagram TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
);