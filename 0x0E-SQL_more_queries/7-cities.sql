-- Task creates a database and a table
-- Script creates a database `hbtn_0d_usa` and the table `cities`
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities`(
       id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
       state_id INT NOT NULL,
       FOREIGN KEY (state_id) REFERENCES states(id),
       name VARCHAR(256) NOT NULL
);
