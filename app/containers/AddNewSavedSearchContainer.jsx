import React from 'react';
import { connect } from 'react-redux';

import { addNewSavedSearch } from '../actions';
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
          }}
          iconName="add_circle"
        />
      </span>
    </li>
  </ul>
);

AddNewSavedSearchComponent.propTypes = {
  onAdd: React.PropTypes.func
};

const mapDispatchToProps = (dispatch) => ({
  onAdd: (newSearch) => dispatch(addNewSavedSearch(newSearch))
});

const AddNewSavedSearch = connect(
  null,
  mapDispatchToProps
)(AddNewSavedSearchComponent);

export default AddNewSavedSearch;
