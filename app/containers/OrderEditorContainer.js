import { connect } from 'react-redux';
import OrderEditor from '../components/OrderEditor';
import { removeFromOrder } from '../actions/';

const mapStateToProps = (state) => ({
  items: state.order.items.sort((a, b) => (
    a.publisher.localeCompare(b.publisher) ||
      a.title.localeCompare(b.title)
    ))
});

const mapDispatchToProps = (dispatch) => ({
  onRemoveItem: (previewsCode) =>
    dispatch(removeFromOrder(previewsCode))
});

const OrderEditorContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(OrderEditor);

export default OrderEditorContainer;
