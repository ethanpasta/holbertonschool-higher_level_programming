-- Task creates a table
-- Script creates a table with a unique id
CREATE TABLE IF NOT EXISTS `unique_id`(
       id INT UNIQUE DEFAULT 1,
       name VARCHAR(256)
);
