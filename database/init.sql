-- Check if the database exists, and create it if not
SELECT 'CREATE DATABASE mydatabase' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mydatabase');

-- Switch to the newly created database
\c mydatabase;

-- Create a table for the task list if it doesn't exist
CREATE TABLE IF NOT EXISTS tasklist (
    id SERIAL PRIMARY KEY,
    taskname VARCHAR(255) NOT NULL,
    completed BOOLEAN NOT NULL
);

-- Insert some sample tasks if the table is empty
INSERT INTO tasklist (taskname, completed) VALUES
    ('Task 1', false),
    ('Task 2', true),
    ('Task 3', false);
