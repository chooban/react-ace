export default function (fn, wait) {
  let timeout;
  return function debounce(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => fn.apply(this, args), (wait || 1));
  };
}
