import React from 'react';
import PropTypes from 'prop-types';
import TextField from 'material-ui/TextField';
import { fade } from 'material-ui/styles/colorManipulator';
import { withStyles } from 'material-ui/styles';
import Icon from 'material-ui/Icon';

const styles = (theme) => ({
  root: {
    fontFamily: theme.typography.fontFamily,
    position: 'relative',
    marginRight: theme.spacing.unit * 2,
    marginLeft: theme.spacing.unit,
    borderRadius: 2,
    background: fade(theme.palette.common.white, 0.15),
    '&:hover': {
      background: fade(theme.palette.common.white, 0.25)
    },
    '& $input': {
      transition: theme.transitions.create('width'),
      width: 200,
      '&:focus': {
        width: 250
      }
    }
  },
  search: {
    width: theme.spacing.unit * 6,
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center'
  },
  input: {
    font: 'inherit',
    padding: `${theme.spacing.unit}px ${theme.spacing.unit}px ${theme.spacing.unit}px ${theme.spacing.unit * 6}px`,
    border: 0,
    display: 'block',
    verticalAlign: 'middle',
    whiteSpace: 'normal',
    background: 'none',
    margin: 0, // Reset for Safari
    color: 'inherit',
    width: '100%',
    '&:focus': {
      outline: 0
    }
  }
});

const SearchComponent = ({ classes, onSearchUpdate, searchValue }) => (
  <div className={classes.root}>
    <div className={classes.search}>
      <Icon>search</Icon>
    </div>
    <TextField
      id="search"
      value={searchValue}
      className={classes.input}
      onInput={(e) => requestAnimationFrame(onSearchUpdate.bind(this, e.target.value))}
    />
  </div>
);

SearchComponent.propTypes = {
  classes: PropTypes.object.isRequired,
  onSearchUpdate: PropTypes.func.isRequired,
  searchValue: PropTypes.string
};

SearchComponent.defaultProps = {
  searchValue: ''
};

export default withStyles(styles)(SearchComponent);
