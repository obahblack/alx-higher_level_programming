-- a script to create a table and fail if it already exists
-- first_table attributes id(int) namevarchar(256)

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
