/* eslint no-shadow: 0 */
import test from 'tape';

import {
  matchesSavedSearches,
  searchCatalogue
} from '../CatalogueSearch';

test('Search function', (t) => {
  const catalogue = [
    {
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
    }
  ];

  t.test('Search covers publisher', (t) => {
    const results = searchCatalogue('marvel', catalogue);
    t.equal(results.length, 2);
    t.equal(results[0].previewsCode, 'ABC/123');
    t.equal(results[1].previewsCode, 'ABC/124');
    t.end();
  });

  t.test('Search covers title', (t) => {
    const results = searchCatalogue('Ber', catalogue);
    t.equal(results.length, 1);
    t.equal(results[0].previewsCode, 'ABC/125');
    t.end();
  });

  t.test('Saved searches match', (t) => {
    const savedSearches = [
      'spider',
      'berlin'
    ];

    t.equal(matchesSavedSearches(savedSearches, catalogue[0]), true);
    t.end();
  });

  t.test('Order does not matter in search', (t) => {
    const search = 'tp harrow county';
    const results = searchCatalogue(search, catalogue);

    t.equal(results.length, 1);
    t.equals(results[0].previewsCode, 'ABC/126');
    t.end();
  });

  t.test('Saved searches do not match', (t) => {
    const savedSearches = [
      'spider',
      'berlin'
    ];

    t.equal(matchesSavedSearches(savedSearches, catalogue[1]), false);
    t.end();
  });
});
