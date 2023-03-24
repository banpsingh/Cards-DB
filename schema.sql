CREATE TABLE decks(
  id INT AUTO_INCREMENT,
  deck_name varchar(70) NOT NULL,
  designer varchar(30),
  manufacturer varchar(30),
  year_made YEAR,
  date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  deck_image BLOB,
  PRIMARY KEY(id)
);

