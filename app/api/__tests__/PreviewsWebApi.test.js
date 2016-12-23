/* eslint no-shadow: 0 */
import fetchMock from 'fetch-mock';
import test from 'tape';

import {
  getLatestIssue
} from '../PreviewsWebApi';

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
      fetchMock.restore();
    });
  });
});
