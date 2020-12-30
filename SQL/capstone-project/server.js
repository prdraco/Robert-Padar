/* Install and import the following packages: body-parser, cors, errorhandler, 
morgan, and express. When installing, ensure they get saved to the dependencies 
in package.json.
Create an instance of an Express app and save it to a variable.
In server.js, import the API router and mount it at all routes starting at /api.*/
const apiRouter = require('./api/api');
const express = require('express');
const app = express();
const morgan = require('morgan');
const bodyParser = require('body-parser');
const cors = require('cors');
const errorhandler = require('errorhandler');

/* Create a variable representing the port your server will listen on. This 
should be able to be optionally set to process.env.PORT if that value is 
set, for testing purposes. Otherwise, it should default to the port number 
of your choice (except 8081 as this is the port the test file uses).*/
const PORT = process.env.PORT || 4000;

/* Use the body-parser JSON, errorhandler, and CORS middleware functions for 
all routes in the server. Additionally consider setting up morgan logging to 
the dev setting for easier debugging.*/
app.use('./api', apiRouter);
app.use(express.static('public'));
app.use(bodyParser.json());
app.use(morgan('tiny'));
app.use(cors());
app.use(errorhandler());

/* Start your server using the port variable you declared earlier. Add 
a callback function that will log out a useful message to the console 
once your server is running.*/
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
})

/* Finally, export the Express app (for use in the test file)*/
module.exports = app;