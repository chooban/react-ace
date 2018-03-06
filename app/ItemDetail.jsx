import React from 'react';
// import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import Reboot from 'material-ui/Reboot';
import { withStyles } from 'material-ui/styles';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';

import ItemPreview from './components/PreviewsItemPreview';

const ItemDetailsComponent = () => (
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
      <ItemPreview previewsCode="341/0001" />
    </main>
  </div>
);

const ItemDetails = connect(null, null)(ItemDetailsComponent);

export default withStyles({})(ItemDetails);

