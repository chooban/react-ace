import React from 'react';
import { connect } from 'react-redux';

const ToggleOrderComponent = ({ previewsCode, ordered, onItemSelected }) => (
  <div
    className="toggleOrder"
  >
    <button
      className={ordered ? 'ordered' : 'notordered'}
      onClick={() => onItemSelected(previewsCode, ordered)}
    >
      Item is { ordered ? '' : ' not ' } on order
    </button>
  </div>
);

ToggleOrderComponent.propTypes = {
  previewsCode: React.PropTypes.string,
  ordered: React.PropTypes.bool,
  onItemSelected: React.PropTypes.func
};

const mapStateToProps = (state, myProps) => ({
  ordered: myProps.ordered
});

const ToggleOrderContainer = connect(
  mapStateToProps
)(ToggleOrderComponent);

export { ToggleOrderComponent };

export default ToggleOrderContainer;
