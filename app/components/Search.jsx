import React from 'react';

const SearchComponent = ({ onSearchUpdate, searchValue }) => (
  <div className="input-field">
    <form>
      <input
        type="search"
        className="searchinput"
        name="search"
        size="25"
        value={searchValue}
        onInput={(e) => requestAnimationFrame(onSearchUpdate.bind(this, e.target.value))}
      />
      <label htmlFor="search">
        <i className="material-icons">search</i>
      </label>
      <i
        className="material-icons"
        onClick={() => {
          const node = document.querySelector('.searchinput');
          node.value = '';
          onSearchUpdate(node.value);
        }}
      >
        cancel
      </i>
    </form>
  </div>
);

SearchComponent.propTypes = {
  onSearchUpdate: React.PropTypes.func.isRequired,
  searchValue: React.PropTypes.string
};

SearchComponent.defaultProps = {
  searchValue: ''
};

export default SearchComponent;
