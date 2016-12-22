import { connect } from 'react-redux';
import OrderView from '../components/OrderView';
import fileDownload from '../utils/FileDownload';
import orderToCsv from '../utils/OrderToCsv';

const mapStateToProps = (state) => ({
  items: state.order.items
});

function exportCurrentOrder() {
  return (dispatch, getStore) => {
    const store = getStore();
    fileDownload(orderToCsv(store.order.items), `order${store.order.issue}.csv`);
  };
}

const OrderViewContainer = connect(
    mapStateToProps,
    { exportCurrentOrder }
)(OrderView);

export default OrderViewContainer;
