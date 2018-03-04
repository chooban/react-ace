export default {
  issues: {
    isFetching: false,
    data: []
  },
  order: {
    issue: undefined,
    items: [],
    total: 0
  },
  gridConfig: {
    pageSize: 20,
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

