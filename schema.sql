CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin INTEGER
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    user_id INTEGER REFERENCES users
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    topic_id INTEGER REFERENCES topics,
    sent_at TIMESTAMP,
    like_count INTEGER
);

CREATE TABLE visitors (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP
);

CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages,
    user_id INTEGER REFERENCES users
);