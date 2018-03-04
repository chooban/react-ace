import React from 'react';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';

import Search from '../containers/SearchContainer';
import OrderView from '../containers/ShoppingCartContainer';

const HeaderBarComponent = () => (
  <AppBar position="static" color="default">
    <Toolbar>
      <Typography align="center" variant="title" color="inherit">
        Ace My Order
      </Typography>
      <Search />
      <OrderView />
    </Toolbar>
  </AppBar>
);

export default HeaderBarComponent;
