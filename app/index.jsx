import './main.css';

import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunkMiddleware from 'redux-thunk';
import createLogger from 'redux-logger';
import app from './reducers';
import { requestIssues } from './actions';
import actors from './actors';

import RootApp from './App.jsx';

let store = createStore(app, applyMiddleware(thunkMiddleware, createLogger()));

actors(store);
store.dispatch(requestIssues());

render(<Provider store={store}>
  <RootApp />
</Provider>,
document.getElementById('app')
);
