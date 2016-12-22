/* eslint no-shadow: 0 */
import fetchMock from 'fetch-mock';
import test from 'tape';

import {
  getIssueList,
  getIssue,
  getLatestIssue
} from '../PreviewsWebApi';

test('Previews API', (t) => {
  t.test('Getting the issue list', (t) => {
    const returnedList = '["337","336","335"]';
    const expectedResult = ['337', '336', '335'];

    fetchMock.get('/api/previews/', returnedList);

    return getIssueList().then((d) => {
      t.deepEqual(d, expectedResult);
      fetchMock.restore();
    });
  });

  t.test('Get an issue', (t) => {
    const returnedData = '{"file":"ecmail337","contents":[{"previewsCode": "337/0001", "title": "Previews Only #339"}]}';
    const expectedResult = [{
      previewsCode: '337/0001',
      title: 'Previews Only #339'
    }];

    fetchMock.get('/api/previews/337', returnedData);
    return getIssue(337).then((d) => {
      t.deepEqual(d, expectedResult);
      fetchMock.restore();
    });
  });

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
