DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id integer primary key autoincrement,
  firstname string not null,
  lastname string not null,
  email string not null
);
