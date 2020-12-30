/* Within api.js, importexpress. Then create an instance of an Express 
router and save it to a variable.
Export the router.*/
const express = require('express');
const apiRouter = express.Router();

const seriesRouter = require('./series.js');

/* In api.js, import the artists router and mount it at /artists.*/
const artistsRouter = require('./artists.js');
apiRouter.use('./artists', artistsRouter);
apiRouter.use('./series', seriesRouter);

module.exports = apiRouter;