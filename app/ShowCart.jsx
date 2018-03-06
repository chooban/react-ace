import React from 'react';
import { connect } from 'react-redux';

import Reboot from 'material-ui/Reboot';
import { withStyles } from 'material-ui/styles';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';

import OrderEditor from './containers/OrderEditorContainer';

const CartContentsComponent = () => (
  <div className="previewsApp">
    <Reboot />
    <header>
      <nav>
        <div className="nav-wrapper container">
          <AppBar position="static" color="default">
            <Toolbar>
              <Typography align="center" variant="title" color="inherit" nowrap="true">
                Ace My Order
              </Typography>
            </Toolbar>
          </AppBar>
        </div>
      </nav>
    </header>
    <main className="content container">
      <OrderEditor />
    </main>
  </div>
);

const CartContents = connect(null, null)(CartContentsComponent);

export default withStyles({})(CartContents);
