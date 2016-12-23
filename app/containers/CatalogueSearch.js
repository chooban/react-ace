export function searchCatalogue(searchTerm, catalogue) {
  const publisherOrTitleMatches = (regex) =>
    (d) => regex.test(d.publisher) || regex.test(d.title);

  const regex = new RegExp(`.*${searchTerm}.*`, 'ig');
  return catalogue.filter(publisherOrTitleMatches(regex));
}
