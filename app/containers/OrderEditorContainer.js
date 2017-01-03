import { connect } from 'react-redux';
import OrderEditor from '../components/OrderEditor';

const mapStateToProps = (state) => ({
  items: state.order.items
});

const mapDispatchToProps = () => ({

});

const OrderEditorContainer = connect(
  mapStateToProps,
  mapDispatchToProps
)(OrderEditor);

export default OrderEditorContainer;
