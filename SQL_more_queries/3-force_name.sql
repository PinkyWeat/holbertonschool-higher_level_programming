-- script creates table force_name on MySQL server with specifics.
CREATE TABLE IF NOT EXISTS  id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);