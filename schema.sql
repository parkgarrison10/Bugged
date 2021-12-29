-- Create tracker database. Ensure Unicode is fully supported.

DROP DATABASE IF EXISTS tracker;

CREATE DATABASE tracker CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

USE tracker;
DROP TABLE IF EXISTS bugs;

CREATE TABLE bugs (
    id SERIAL PRIMARY KEY,
    description TEXT,
    project TEXT,
    priority TEXT,
    entry_date TEXT,
    resolved INT
);