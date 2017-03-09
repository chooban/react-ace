import React from 'react';
import { connect } from 'react-redux';

import { addSavedSearch } from '../actions';
import ClickableIcon from '../components/ClickableIcon';

const AddNewSavedSearchComponent = ({ onAdd }) => (
  <ul className="collection addnewsearch">
    <li className="collection-item">
      <span
        className="primary-content"
      >
        <input
          type="text"
          placeholder="Add new search term"
          className="addnewsearch"
          onKeyUp={(e) => {
            if (e.keyCode === 13) {
              const input = document.querySelector('input.addnewsearch');
              onAdd(input.value);
              input.value = '';
            }
          }}
        />
      </span>
      <span
        className="secondary-content"
      >
        <ClickableIcon
          className="addnewsearch"
          onClick={() => {
            const input = document.querySelector('input.addnewsearch');
            onAdd(input.value);
            input.value = '';
          }}
          iconName="add_circle"
        />
      </span>
    </li>
  </ul>
);

AddNewSavedSearchComponent.propTypes = {
  onAdd: React.PropTypes.func.isRequired
};

const mapDispatchToProps = (dispatch) => ({
  onAdd: (newSearch) => dispatch(addSavedSearch(newSearch))
});

const AddNewSavedSearch = connect(
  null,
  mapDispatchToProps
)(AddNewSavedSearchComponent);

export default AddNewSavedSearch;
