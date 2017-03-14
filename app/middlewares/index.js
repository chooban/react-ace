import thunkMiddleware from 'redux-thunk';

import savedSearchMiddleware from './SavedSearchObserver';
import exportOrderMiddleware from './ExportOrderObserver';

const middlewares = [thunkMiddleware];
if (process.env.NODE_ENV === 'development') {
const createLogger = require('redux-logger'); //eslint-disable-line
  const loggerConfig = {
    level: 'error'
  };
  middlewares.push(createLogger(loggerConfig));
}

middlewares.push(exportOrderMiddleware);
middlewares.push(savedSearchMiddleware);

export default middlewares;
