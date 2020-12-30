/* Install sqlite3. We’re going to need to use an older version of sqlite3, so use the following command:
npm install sqlite3@^3
Inside sql.js, import the sqlite3 library.*/
const sqlite3 = require('sqlite3');

/* Still in sql.js, create a const db and create a new sqlite3.Database at './db.sqlite'.*/
const db = new sqlite3.Database('./db.sqlite');

/* Use your db to create a table called Strip with the following schema:
id, an integer as the primary key.
head, a not-null text column.
body, a not-null text column.
background, a not-null text column.
bubble_type, a non-null text column.
bubble_text, a not-null text column that defaults to an empty string.
caption, a not-null text column that defaults to an empty string.*/
db.run(`CREATE TABLE Strip (
  id INTEGER PRIMARY KEY,
  head TEXT NOT NULL,
  body TEXT NOT NULL,
  background TEXT NOT NULL,
  bubble_type TEXT NOT NULL,
  bubble_text TEXT NOT NULL DEFAULT '',
  caption TEXT NOT NULL DEFAULT ''
)`);