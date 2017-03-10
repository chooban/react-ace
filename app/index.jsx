import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware, compose } from 'redux';
import thunkMiddleware from 'redux-thunk';

import app from './reducers';
import { requestLatestIssue } from './actions';
import actors from './actors';
import savedSearchMiddleware from './middlewares/SavedSearchObserver';
import './main.css';

import RootApp from './App';

function run() {
  const middlewares = [thunkMiddleware];

  if (process.env.NODE_ENV === 'development') {
  const createLogger = require('redux-logger'); //eslint-disable-line
    const loggerConfig = {
      level: 'error'
    };
    middlewares.push(createLogger(loggerConfig));
  }

  middlewares.push(savedSearchMiddleware);

  const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  const store = createStore(app, composeEnhancers(applyMiddleware(...middlewares)));

  actors(store);
  store.dispatch(requestLatestIssue());

  render(<Provider store={store}><RootApp /></Provider>, document.getElementById('app'));
}

// Just make an assumption base on one missing function.
if (!Object.assign) {
  require.ensure([], () => {
    require('babel-polyfill'); //eslint-disable-line
    run();
  }, 'polyfill');
} else {
  run();
}

