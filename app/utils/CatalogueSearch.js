export function searchCatalogue(searchTerm, catalogue) {
  const publisherOrTitleMatches = (regex) =>
    (d) => regex.test(d.title) || regex.test(d.publisher);

  const regex = new RegExp(searchTerm, 'i');

  return catalogue.filter(publisherOrTitleMatches(regex));
}

export function matchesSavedSearches(searchTerms, item) {
  const publisherOrTitleMatches = (regex) =>
    (d) => regex.test(d.title) || regex.test(d.publisher);

  return searchTerms.some((searchTerm) => {
    const regex = new RegExp(searchTerm, 'i');
    return publisherOrTitleMatches(regex)(item);
  });
}
