-- create a database(hbtn_0d_usa) and the table cities
-- description of table data:
-- 	id (INT unique, auto generated, can't be null and is a primary key)
-- 	state_id (INT, NOT NULL & must be a FOREIGN KEY that references to id of the states table
-- 	name (VARCHAR(256))

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF  NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);