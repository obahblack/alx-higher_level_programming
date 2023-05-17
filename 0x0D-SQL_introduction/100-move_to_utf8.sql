-- a script thta converts hbtn_0c_0 database to UTF8
-- convert Table (first_table) to UTF8
-- convert field(name) in first_table to Utf8

-- convert the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- selct the database
USE hbtn_0c_0;

-- convert the table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- convert the field
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
