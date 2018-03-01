import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from 'material-ui/styles';
import Icon from 'material-ui/Icon';
import Badge from 'material-ui/Badge';

const styles = (theme) => ({
  margin: {
    margin: theme.spacing.unit * 2
  },
  padding: {
    padding: `0 ${theme.spacing.unit * 2}px`
  }
});

const ShoppingCartIcon = ({ classes, count, onClick }) => (
  <div>
    <Badge
      className={classes.margin}
      badgeContent={count}
      color="primary"
    >
      <Icon>shopping_cart</Icon>
    </Badge>
  </div>
);

ShoppingCartIcon.propTypes = {
  classes: PropTypes.object.isRequired,
  onClick: PropTypes.func,
  count: PropTypes.number
};

ShoppingCartIcon.defaultProps = {
  onClick: () => ({}),
  count: 0
};
export default withStyles(styles)(ShoppingCartIcon);
