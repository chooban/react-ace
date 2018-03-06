import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from 'material-ui/styles';
import Icon from 'material-ui/Icon';
import Badge from 'material-ui/Badge';
import Typography from 'material-ui/Typography';

const styles = (theme) => ({
  root: {
    fontFamily: theme.typography.fontFamily,
    position: 'relative',
    marginRight: theme.spacing.unit * 2,
    marginLeft: theme.spacing.unit,
    display: 'flex'
  },
  inner: {
    marginRight: `${theme.spacing.unit}px`
  }
});

const formatAsGBP = (v) => ((v) ? `£${parseFloat(v).toFixed(2)}` : '£0');

const ShoppingCartIcon = ({
  classes,
  count,
  orderTotal,
  onClick
}) => (
  <div className={classes.root}>
    <Badge
      className={classes.inner}
      badgeContent={count}
      color="secondary"
      onClick={onClick}
    >
      <Icon
        className={classes.inner}
        component="div"
      >
        shopping_basket
      </Icon>
    </Badge>
    <Typography variant="subheading" className={classes.inner}>
      {formatAsGBP(orderTotal)}
    </Typography>
  </div>
);

ShoppingCartIcon.propTypes = {
  classes: PropTypes.object.isRequired,
  onClick: PropTypes.func,
  count: PropTypes.number,
  orderTotal: PropTypes.number
};

ShoppingCartIcon.defaultProps = {
  onClick: () => ({}),
  count: 0,
  orderTotal: 0
};
export default withStyles(styles)(ShoppingCartIcon);
