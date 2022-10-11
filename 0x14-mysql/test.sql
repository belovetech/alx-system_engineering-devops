-- task 1
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- task 2
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 ( id int, Name varchar(255) );
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
INSERT INTO nexus6 (id, name) VALUES (1, "Beloved");

-- task3
CREATE USER IF NOT EXISTS replica_user@'%' IDENTIFIED BY 'replica_passwd';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'replica_passwd';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
