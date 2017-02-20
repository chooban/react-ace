/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import * as actions from '../../actions';
import {
  mapStateToProps,
  mapDispatchToProps
} from '../SavedSearchesListContainer';

const catalogue = [{
  previewsCode: 'ABC/123',
  publisher: 'Marvel',
  title: 'Spider-Man'
}, {
  previewsCode: 'ABC/124',
  publisher: 'DC Comics',
  title: 'Marvelman'
}, {
  previewsCode: 'ABC/125',
  publisher: 'Drawn & Quarterly',
  title: 'Berlin'
}, {
  previewsCode: 'ABC/126',
  publisher: 'Dark Horse',
  title: 'Harrow County TP 01 Countless Haints'
}, {
  previewsCode: 'ABC/127',
  publisher: 'Dark Horse',
  title: 'Lone Wolf and Cub 7'
}, {
  previewsCode: 'ABC/128',
  publisher: 'Dark Horse',
  title: 'Lone Wolf and Cub 8'
}];

test('Saved searches list container', (t) => {
  t.test('Empty list returned if no profile', (t) => {
    const state = {
      user: {
        profile: null
      }
    };
    const props = mapStateToProps(state);

    t.deepEqual(props.savedSearches, []);
    t.end();
  });

  t.test('Profile searches applied', (t) => {
    const state = {
      user: {
        profile: {
          savedsearches: [
            'spider-man',
            'lone wolf'
          ]
        }
      },
      issues: {
        data: catalogue
      }
    };

    const props = mapStateToProps(state);

    t.deepEqual(props.savedSearches, [
      {
        searchTerm: 'lone wolf',
        hits: 2
      },
      {
        searchTerm: 'spider-man',
        hits: 1
      }
    ]);
    t.end();
  });

  t.test('Searches can be deleted', (t) => {
    const dispatchSpy = sinon.spy();
    const actionSpy = sinon.spy(actions, 'deleteSavedSearch');
    const props = mapDispatchToProps(dispatchSpy);

    t.ok(props.onDelete);

    props.onDelete('lone wolf');

    t.ok(dispatchSpy.calledOnce);
    t.ok(actionSpy.calledOnce, true);
    t.ok(actionSpy.calledWith('lone wolf'));
    t.end();
  });

  t.test('Searches can be selected', (t) => {
    const dispatchSpy = sinon.spy();
    const actionSpy = sinon.spy(actions, 'performSavedSearch');
    const props = mapDispatchToProps(dispatchSpy);

    t.ok(props.onSelect);

    props.onSelect('lone wolf');

    t.ok(dispatchSpy.calledOnce);
    t.ok(actionSpy.calledOnce, true);
    t.ok(actionSpy.calledWith('lone wolf'));
    t.end();
  });
});
