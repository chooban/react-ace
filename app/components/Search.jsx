import React from 'react';

const SearchComponent = ({ onSearchUpdate }) => (
  <div className="gridsearch">
    <label
      htmlFor="search"
    >
      <i className="fa fa-search fa-lg" aria-hidden="true" />
      <input
        type="text"
        name="search"
        placeholder="Search"
        size="25"
        onInput={(e) => onSearchUpdate(e.target.value)}
      />
    </label>
  </div>
);

SearchComponent.propTypes = {
  onSearchUpdate: React.PropTypes.func
};

export default SearchComponent;
