import React from 'react';

const SavedSearchesList = ({ savedSearches, onDelete, onSelect }) => (
  <ul className="collection savedsearches">
    {savedSearches.map((key, idx) => (
      <li
        className="collection-item"
        key={idx}
      >
        <span
          className="primary-content"
          onClick={() => onSelect(key)}
        >
          <i
            className="material-icons"
          >
            search
          </i>
          <span className="title">
            {key}
          </span>
        </span>
        <span
          className="secondary-content"
        >
          <i
            style={{ color: 'black' }}
            className="material-icons"
            onClick={() => onDelete(key)}
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
  onDelete: React.PropTypes.func,
  onSelect: React.PropTypes.func
};

export default SavedSearchesList;
