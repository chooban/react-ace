/* eslint no-shadow: 0 */
import test from 'tape';
import sinon from 'sinon';

import {
  mapStateToProps,
  mapDispatchToProps
} from '../SavedSearchesContainer';

import { closeSavedSearches } from '../../actions';

test('Saved searches props', (t) => {
  t.test('Props has close dispatch callback', (t) => {
    const dispatchSpy = sinon.spy();

    const props = mapDispatchToProps(dispatchSpy);
    props.close();

    t.ok(dispatchSpy.calledOnce);
    t.ok(dispatchSpy.calledWith(closeSavedSearches()));
    t.end();
  });

  t.test('Props has display flag', (t) => {
    [true, false].forEach((b) => {
      const state = {
        ui: {
          showSavedSearches: b
        },
        user: {}
      };
      const props = mapStateToProps(state);
      t.equal(props.display, b);
    });
    t.end();
  });

  t.test('No searches to show', (t) => {
    const state = {
      ui: {
        showSavedSearches: true
      },
      user: {
        profile: {
          nickname: 'chooban',
          savedsearches: []
        }
      }
    };

    const props = mapStateToProps(state);
    t.notOk(props.hasSearches);
    t.end();
  });

  t.test('Searches to show', (t) => {
    const state = {
      ui: {
        showSavedSearches: true
      },
      user: {
        profile: {
          nickname: 'chooban',
          savedsearches: ['dredd']
        }
      }
    };

    const props = mapStateToProps(state);
    t.ok(props.hasSearches);
    t.end();
  });
});
