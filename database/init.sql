-- Active: 1705881420387@@127.0.0.1@3306
-- init.sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    status INTEGER NOT NULL CHECK (status IN (0, 1))
);

INSERT INTO tasks (task_name, status) VALUES
    ('Task 1', 1),
    ('Task 2', 0),
    ('Task 3', 1);
