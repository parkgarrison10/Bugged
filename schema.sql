-- Create dealership database and user. Ensure Unicode is fully supported.

CREATE DATABASE IF NOT EXISTS tracker CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

USE tracker;
DROP TABLE IF EXISTS bugs;

CREATE TABLE bugs (
    id SERIAL PRIMARY KEY,
    identifier INT,
    description TEXT,
    project TEXT,
    priority TEXT,
    entry_date DATETIME,
    resolved INT
);

INSERT INTO bugs(identifier, description, project, priority, entry_date, resolved) 
 VALUES (1, "Testing Database Creation", "Bugged", "high", "2021-12-27 17:02:36", 0);