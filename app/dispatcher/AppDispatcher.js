import { Dispatcher } from 'flux';
import assign from 'object-assign';

export default assign(new Dispatcher(), {
  handleAction(action) {
    console.log('Dispatching', action);
    this.dispatch({
      action: action,
    });
    console.log('Dispatched', action);
  },
});
