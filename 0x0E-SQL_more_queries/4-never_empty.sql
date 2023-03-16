-- Creates the table id_not_null if it does not already exist, with: id and name.
 
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT NOT NULL DEFAULT 1,
  name VARCHAR(256)
) ENGINE=InnoDB;