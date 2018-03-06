import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware, compose } from 'redux';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import app from './reducers';
import middlewares from './middlewares/';
import { requestLatestIssue } from './actions';
import actors from './actors';
import initialStateFactory from './reducers/InitialStateFactory';

import RootApp from './App';
import ShowCart from './ShowCart';
import ItemDetail from './ItemDetail';

export default function () {
  const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  const store = createStore(
    app,
    initialStateFactory(),
    composeEnhancers(applyMiddleware(...middlewares))
  );

  actors(store);
  store.dispatch(requestLatestIssue());
  render(
    <Provider store={store}>
      <Router>
        <Switch>
          <Route exact path="/" component={RootApp} />
          <Route path="/cart" component={ShowCart} />
          <Route path="/details/" component={ItemDetail} />
        </Switch>
      </Router>
    </Provider>,
    document.getElementById('app')
  );
}

