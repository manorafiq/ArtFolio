-- Users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    profession TEXT NOT NULL,
    bio TEXT,
    profile_image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    category TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- visibility TEXT CHECK(visibility IN ('public', 'private', 'unlisted')) DEFAULT 'public',
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- Images table (for project images)
CREATE TABLE images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    file_type TEXT NOT NULL,
    is_cover_image BOOLEAN DEFAULT 0,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE
);

-- Social media links table
CREATE TABLE social_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    platform TEXT NOT NULL,
    url TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- Create indexes for better query performance
CREATE INDEX idx_projects_user_id ON projects (user_id);
CREATE INDEX idx_images_project_id ON images (project_id);
CREATE INDEX idx_social_links_user_id ON social_links (user_id);

-- CREATE TABLE users (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT NOT NULL,
--     email TEXT NOT NULL UNIQUE,
--     password TEXT NOT NULL,
--     name TEXT NOT NULL,
--     profession TEXT NOT NULL,
-- );

-- CREATE TABLE projects (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     title TEXT NOT NULL,
--     description TEXT,
--     images BLOB NOT NULL,
--     uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     user_id INTEGER NOT NULL,
--     FOREIGN KEY (user_id) REFERENCES users (id)
-- );

-- CREATE TABLE socials (
--     user_id INTEGER NOT NULL,
--     facebook TEXT,
--     twitter TEXT,
--     linedin TEXT,
--     pintrest TEXT,
--     instagram TEXT,
--     FOREIGN KEY (user_id) REFERENCES users (id)
-- );