import React from 'react';

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
      <i
        className="material-icons cancelsearch"
        style={{
          visibility: (searchValue.length > 1) ? null : 'hidden'
        }}
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
