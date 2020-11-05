/* Create and export your Express app from a root-level file called server.js*/
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');
const errorhandler = require('errorhandler');
/* Accept and set an optional port argument for your server*/
const PORT = process.env.PORT || 4000;

const apiRouter = require('./api/api');

app.use(express);
app.use(bodyParser.json());
app.use(cors());

app.use('/api', apiRouter);

app.use(errorhandler());


/* to listen on from process.env.PORT*/
app.listen(PORT, () => {
    consloe.log(`Server is listening on ${PORT}`);
});

module.exports = app;