/* Inside app.js, import Express and create an instance of an Express server called app. Use module.exports to export app.*/
const express = require('express');
const app = express();
/* npm install, import and app.use() body-parsing middleware to parse JSON bodies. Add logging middleware as well (use whatever format of logging that you want).*/
const bodyParser = require('body-parser');
const morgan = require('morgan');
const sqlite3 = require('sqlite3');
module.exports = app;

/* Serve the Codestrips site with app.use(express.static('public'));*/
app.use(express.static('public'));
app.use(bodyParser.json());
app.use(morgan('tiny'));

/* Import your SQLite database into app.js. You’ll need to require the sqlite3 package, assign it to a constant variable named sqlite3, and create a database variable named db.*/
const db = new sqlite3.Database(process.env.TEST_DATABASE || './db.sqlite');
/* Create a const PORT and set it equal to process.env.PORT || 4001.*/
const PORT = process.env.PORT || 4001;

/* In app.js, add a new route to your application. This new route should monitor the /strips endpoint for GET requests.*/
app.get('/strips', (req, res, next) => {
  /* When a GET request is sent to /strips, get an array of all strips from the Strip table.*/
  db.all(`SELECT * FROM Strip`, (error, rows) => {
    if(error) {
      res.sendStatus(500);
    } else { /* Send back the array of all strips in the db.all() callback. Create an object to send in the response and set its strips property equal to the rows returned from the database.*/
      res.send({ strips: rows });
    }
  });
});

/* When a POST /strips request arrives, the application should validate the strip and send a 400 response if it is invalid.*/
const validateStrip = (req, res, next) => {
  const stripToCreate = req.body.strip;
  if(!stripToCreate.head ||
      !stripToCreate.body ||
      !stripToCreate.bubleType ||
      !stripToCreate.background) {
        return res.status(400);
  }
  next();
}

/* In app.js, add a new route to your application. The new route should monitor the /strips endpoint for POST requests.*/
app.post('/strips', validateStrip, (req, res, next) => {

/*The new Strip will arrive as a strip property on the request body. Here is an example req.body.strip:
{
  head: 'happy',
  body: 'plus',
  background: 'boat'
  bubbleType: 'statement',
  bubbleText: 'Hello, world!',
  caption: 'Test strip'
}
head, body, background, and bubbleType are required. bubbleText and caption have default values (empty string), so they do not need to be validated by the server before being sent to the database in this case. Send a 400 status code if any of the required values are not present in the request.

Your POST /strips route should INSERT a new strip into the database using the req.body.strip values.*/
  const stripToCreate = req.body.strip;
  db.run(
  `INSERT INTO Strip (
    head, body, bubble_type, background, bubble_text, caption
  ) VALUES ($head, $body, $bubbleType, $background, $bubbleText $caption)`, {
    $head: stripToCreate.head,
    $body: stripToCreate.body,
    $bubbleType: stripToCreate.bubbleType,
    $background: stripToCreate.background,
    $bubbleText: stripToCreate.bubbleText,
    $caption: stripToCreate.caption
  }, /* In your INSERT callback, if an error occurs, send back a 500 response status.*/function(err) {
    if(err) {
      return res.sendStatus(500);
      /* Find the newly-created strip if no error occurred. You’ll have to get the proper row from the database with another query.*/
    } db.get(`SELECT * From Script WHERE id = ${this.lastID}`, (err, row) => {
      if(!row) {
        return res.sendStatus(500);
        /* Set a 201 status code and the send the created strip inside the callback of your db.get(). Create an object to send in the response and set its strip property equal to the strip returned from the database. Send this object in the response.*/
      } res.Status(201).send({ strip: row });
    })
  }
  )
})

app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});