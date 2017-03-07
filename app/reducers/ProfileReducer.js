import initialState from './InitialState';

export default function profileReducer(state = initialState.user, action) {
  switch (action.type) {
    case 'SET_USER_PROFILE': {
      const profile = {
        nickname: action.payload.nickname,
        savedsearches: action.payload.user_metadata ?
          action.payload.user_metadata.saved_searches :
          []
      };
      return Object.assign({}, state, {
        profile
      });
    }
    case 'LOGOUT':
      return Object.assign({}, state, {
        profile: null
      });
    case 'DELETE_SAVED_SEARCH': {
      const searches = state.profile.savedsearches.slice(0);
      const idx = searches.indexOf(action.payload);
      if (idx > -1) {
        searches.splice(idx, 1);
      }
      const profile = Object.assign({}, state.profile, {
        savedsearches: searches
      });
      return Object.assign({}, state, {
        profile
      });
    }
    case 'ADD_SAVED_SEARCH': {
      const searches = state.profile.savedsearches.concat(action.payload);
      const profile = Object.assign({}, state.profile, {
        savedsearches: searches
      });
      return Object.assign({},
        state, {
          profile
        });
    }
    default: return state;
  }
}

