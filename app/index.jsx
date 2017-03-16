import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware, compose } from 'redux';

import app from './reducers';
import middlewares from './middlewares/';
import { requestLatestIssue } from './actions';
import actors from './actors';
import './main.css';
import initialStateFactory from './reducers/InitialStateFactory';

import RootApp from './App';

function run() {
  const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  const store = createStore(
    app,
    initialStateFactory(),
    composeEnhancers(applyMiddleware(...middlewares))
  );

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

