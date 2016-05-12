// jscs:disable
import test from 'tape';
import sinon from 'sinon';
import {inspect} from 'util';
import {CHANGE_EVENT, ADD_TO_ORDER, REMOVE_FROM_ORDER, CHANGED_ISSUE} from '../../consts';

test.only('OrderStore', (t) => {

  t.test('Adding an item to the store', (t) => {
    const AppDispatcher = require('../../dispatcher/AppDispatcher');
    const OrderStore = require('../OrderStore');
    console.log(AppDispatcher);
    const registeredCallback = AppDispatcher.default._callbacks['ID_1'];

    registeredCallback({
      actionType: ADD_TO_ORDER,
      issueNumber: '330',
      previewsCode: '330/0001',
    });
    t.end();
  });
});
