import initialState from './InitialState';
import issues from './IssuesReducer';
import user from './ProfileReducer';
import order from './OrderReducer';
import gridConfig from './GridConfigReducer';
import ui from './UserInterfaceReducer';

export default function app(state = initialState, action) {
  return {
    issues: issues(state.issues, action),
    order: order(state.order, action),
    gridConfig: gridConfig(state.gridConfig, action),
    ui: ui(state.ui, action),
    user: user(state.user, action)
  };
}
