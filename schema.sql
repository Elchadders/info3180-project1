DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id integer primary key autoincrement,
  firstname string not null,
  lastname string not null,
  age integer not null,
  gender string not null,
  biography string not null,
  image file not null,
);