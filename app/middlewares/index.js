import thunkMiddleware from 'redux-thunk';

import savedSearchMiddleware from './SavedSearchObserver';
import exportOrderMiddleware from './ExportOrderObserver';
import saveOrderMiddleware from './SaveOrderObserver';
import removeOldOrderMiddleware from './RemoveOldOrderObserver';

const middlewares = [thunkMiddleware];
if (process.env.NODE_ENV === 'development') {
  const createLogger = require('redux-logger').createLogger; //eslint-disable-line
  const loggerConfig = {
    level: 'error'
  };
  middlewares.push(createLogger(loggerConfig));
}

middlewares.push(exportOrderMiddleware);
middlewares.push(savedSearchMiddleware);
middlewares.push(saveOrderMiddleware());
middlewares.push(removeOldOrderMiddleware);

export default middlewares;
