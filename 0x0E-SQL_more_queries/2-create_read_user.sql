-- a script that creates a database(hbtn_0d_2) and user(user_0d_2)
-- user_0d_2 should have only SELECT privilage in the hbtn_0d_2 database
-- user_0d_2 password should be set to user_0d_2_pwd

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES
