export default {
  issues: {
    isFetching: false,
    data: []
  },
  order: {
    issue: undefined,
    items: []
  },
  gridConfig: {
    pageSize: 25,
    page: 1,
    searchTerm: undefined
  },
  ui: {
    showOrder: false,
    showItemPreview: false,
    showHelp: false,
    itemPreview: undefined,
    showSavedSearches: false
  },
  user: {
    profileFetched: false,
    profile: {
      nickname: null,
      savedsearches: []
    }
  }
};

