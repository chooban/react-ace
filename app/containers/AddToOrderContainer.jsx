import React from 'react';
import { connect } from 'react-redux';
import AddToOrder from '../components/AddToOrder.jsx';

const mapStateToProps = (state) => {
  return {};
}

const mapDispatchToProps = (dispatch) => {
  return {};
}

const AddToOrderContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(AddToOrder);

export default AddToOrderContainer;
