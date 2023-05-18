-- a script that create a table with an ID(int) and a name(VARCHAR) but can't be null

CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
