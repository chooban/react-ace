
import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunkMiddleware from 'redux-thunk';
import createLogger from 'redux-logger';
import app from './reducers';
import { requestLatestIssue } from './actions';
import actors from './actors';
import './main.css';

import RootApp from './App';

const loggerConfig = {
  level: 'error'
};

const store = createStore(app, applyMiddleware(thunkMiddleware, createLogger(loggerConfig)));

actors(store);
store.dispatch(requestLatestIssue());

render(<Provider store={store}>
  <RootApp />
</Provider>,
document.getElementById('app')
);
