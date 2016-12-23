/* eslint no-shadow: 0 */
import test from 'tape';

import { searchCatalogue } from '../CatalogueSearch';

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
});
