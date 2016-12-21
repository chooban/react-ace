import { connect } from 'react-redux';
import OrderView from '../components/OrderView';

const mapStateToProps = (state) => ({
  items: state.order.items
});

function processAndExportOrder() {
  return (dispatch, getState) => {
    const orderItems = getState().order.items;
    const catalogue = getState().issues.data;

    const order = [];
    orderItems.forEach((code) => {
      const item = catalogue.find((d) => d.previewsCode === code);
      order.push({
        previews: code,
        quantity: 1,
        title: item.title,
        price: item.price,
        publisher: item.publisher,
        comment: ''
      });
    });
    console.log(order);
  };
}

const OrderViewContainer = connect(
    mapStateToProps,
    { exportOrder: processAndExportOrder }
)(OrderView);

export default OrderViewContainer;
