import React from 'react';
import ReactDOM from 'react-dom';

export default React.createClass({
  displayName: 'AddToOrder',
  propTypes: {
    checked: React.PropTypes.bool, onChange: React.PropTypes.func,
  },
  onChange(e) {
    this.props.onChange(e.target.checked);
  },

  render() {
    return (
      <input
          type="checkbox"
          onChange={this.onChange}
          checked={this.props.checked}
      />
    );
  },
});
