import React from 'react';
import PropTypes from 'prop-types';

const SearchComponent = ({ onSearchUpdate, searchValue }) => (
  <div className="searchbox">
    <form>
      <label htmlFor="search">
        <i className="material-icons">search</i>
      </label>
      <input
        type="search"
        className="searchinput"
        name="search"
        id="search"
        size="25"
        placeholder="Enter title..."
        value={searchValue}
        onInput={(e) => requestAnimationFrame(onSearchUpdate.bind(this, e.target.value))}
      />
    </form>
  </div>
);

SearchComponent.propTypes = {
  onSearchUpdate: PropTypes.func.isRequired,
  searchValue: PropTypes.string
};

SearchComponent.defaultProps = {
  searchValue: ''
};

export default SearchComponent;
