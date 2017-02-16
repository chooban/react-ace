import React from 'react';

const SavedSearchesList = ({ savedSearches, onDelete }) => (
  <ul className="collection">
    {savedSearches.map((key, idx) => (
      <li
        className="collection-item"
        key={idx}
      >
        {key}
        <span
          className="secondary-content"
        >
          <a
            href="#!"
            onClick={() => onDelete(key)}
          >
            <i
              style={{ color: 'black' }}
              className="material-icons"
            >
              delete
            </i>
          </a>
        </span>
      </li>
    ))}
  </ul>
);

SavedSearchesList.propTypes = {
  savedSearches: React.PropTypes.array,
  onDelete: React.PropTypes.func
};

export default SavedSearchesList;
