const triggers = [
  'EXPORT_ORDER',
  'SET_USER_PROFILE'
];

export default () => (next) => (action) => {
  if (triggers.includes(action.type)) {
    switch (action.type) {
      case 'EXPORT_ORDER':
        ga('send', 'event', 'order', 'export'); // eslint-disable-line
        break;
      case 'SET_USER_PROFILE':
        ga('send', 'event', 'user', 'login'); // eslint-disable-line
        break;
      default:
        break;
    }
  }
  return next(action);
};
