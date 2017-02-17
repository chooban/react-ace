export function searchCatalogue(searchTerm, catalogue) {
  const publisherOrTitleMatches = (regex) =>
    (d) => regex.test(`${d.title} ${d.publisher}`);

  const terms = searchTerm.split(' ');
  const regex = terms
    .map((t) => `(?=.*${t})`)
    .reduce((a, b) => a + b, '');

  const re = new RegExp(regex, 'i');

  return catalogue.filter(publisherOrTitleMatches(re));
}

export function matchesSavedSearches(searchTerms, item) {
  const publisherOrTitleMatches = (regex) =>
    (d) => regex.test(d.title) || regex.test(d.publisher);

  return searchTerms.some((searchTerm) => {
    const regex = new RegExp(searchTerm, 'i');
    return publisherOrTitleMatches(regex)(item);
  });
}
