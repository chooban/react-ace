import React from 'react';

const SavedSearchesList = ({ savedSearches, onDelete, onSelect }) => (
  <ul className="collection savedsearches">
    {savedSearches.map((searchData) => (
      <li
        className="collection-item"
        key={searchData.searchTerm}
      >
        <span
          className="primary-content"
          onClick={() => onSelect(searchData.searchTerm)}
        >
          <i
            className="material-icons"
          >
            search
          </i>
          <span className="title">
            {searchData.searchTerm}
          </span>
          &nbsp;
          <span>
            (
            {searchData.hits}
            )
          </span>
        </span>
        <span
          className="secondary-content"
        >
          <i
            style={{ color: 'black' }}
            className="material-icons"
            onClick={() => onDelete(searchData.searchTerm)}
          >
            delete
          </i>
        </span>
      </li>
    ))}
  </ul>
);

SavedSearchesList.propTypes = {
  savedSearches: React.PropTypes.array.isRequired,
  onDelete: React.PropTypes.func.isRequired,
  onSelect: React.PropTypes.func.isRequired
};

export default SavedSearchesList;
