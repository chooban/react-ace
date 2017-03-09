export default (function (root, factory) { //eslint-disable-line
  module.exports = factory();
}(this, () => function (callback, delay) { //eslint-disable-line
  let timeout;
  return function (...args) { //eslint-disable-line
    const context = this;
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      callback.apply(context, args);
    }, delay);
  };
}));
