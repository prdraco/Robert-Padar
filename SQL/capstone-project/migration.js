/* Import sqlite3. It should already be installed from when you ran 
npm install sqlite3@^3 at the beginning of the project.*/
const sqlite3 = require('sqlite3');

/*Open the database.sqlite file as a sqlite3 database object and save it 
to a variable db.*/
const db = new sqlite3.Database('./database.sqlite');

/*On the database object, run a SQLite command to create an Artist table 
(if it doesn’t already exist) with the following schema:

id - Integer, primary key, required
name - Text, required
date_of_birth - Text, required
biography - Text, required
is_currently_employed - Integer, defaults to 1*/
db.serialize(() => {
    db.run("DROP TABLE Artist");
    db.run("CREATE TABLE IF NOT EXISTS `Artist` ( " +
        " `id` INTEGER NOT NULL PRIMARY KEY, " +
        " `name` TEXT NOT NULL, " +
        " `date_of_birth` TEXT NOT NULL, " +
        " `biography` TEXT NOT NULL, " +
        " `is_currently_employed` INTEGER NOT NULL DEFAULT 1 )");
    /* Now, let’s move on to our next model. Open migration.js and write the 
    code to create a new table called Series, if one doesn’t already exist. 
    The table should have the following column properties:
    id - Integer, primary key, required
    name - Text, required
    description - Text, required*/
    db.run("DROP TABLE Series");
    db.run("CREATE TABLE IF NOT EXISTS `Series` ( " +
        " `id` INTEGER NOT NULL PRIMARY KEY, " +
        " `name` TEXT NOT NULL, " +
        " `description` TEXT NOT NULL )");
    /* Let’s move on to our last model. Open migration.js and write the code to create 
    a new table called Issue, if one doesn’t already exist. The table should have the 
    following column properties:
        id - Integer, primary key, required
        name - Text, required
        issue_number - Integer, required
        publication_date - Text, required
        artist_id - Integer, foreign key, required
        series_id - Integer, foreign key, required*/
    db.run("DROP TABLE Issue");
    db.run("CREATE TABLE IF NOT EXISTS `Issue` ( " +
        " `id` INTEGER NOT NULL PRIMARY KEY, " +
        " `name` TEXT NOT NULL, " +
        " `issue_number` INTEGER NOT NULL, " +
        " `publication_date` TEXT NOT NULL, " +
        " `artist_id` INTEGER NOT NULL, " +
        " `series_id` INTEGER NOT NULL, " +
        " FOREIGN KEY(`artist_id`) REFERENCES `Artist`(`id`), " +
        " FOREIGN KEY(`series_id`) REFERENCES `Series`(`id`))");
});