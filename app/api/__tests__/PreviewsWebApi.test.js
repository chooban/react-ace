/* eslint no-shadow: 0 */
import fetchMock from 'fetch-mock';
import test from 'tape';

import { getLatestIssue } from '../PreviewsWebApi';

test('Previews API', (t) => {
  t.test('Get the latest', (t) => {
    const returnedData = '{"file":"ecmail337","contents":[{"previewsCode": "337/0001", "title": "Previews Only #339"}]}';
    const expectedResult = {
      file: 'ecmail337',
      contents: [{
        previewsCode: '337/0001',
        title: 'Previews Only #339'
      }]
    };

    fetchMock.get('/api/previews/latest', returnedData);

    return getLatestIssue().then((d) => {
      t.deepEqual(d, expectedResult);
      t.equal(fetchMock.done(), true);
      fetchMock.restore();
    });
  });

  t.test('Errors propagate', (t) => {
    fetchMock.get('/api/previews/latest', 403);

    return getLatestIssue().then(() => {
      fetchMock.restore();
      t.fail('Should have thrown an error');
    }).catch((d) => {
      fetchMock.restore();
      t.ok(d instanceof Error, 'Was not an error');
    });
  });
});
