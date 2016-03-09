import React from 'react'
import {getIssue} from '../actions/PreviewsActions'
import PreviewsStore from '../stores/PreviewsStore'
import {Table} from 'reactabular'
import Paginator from 'react-pagify'
import segmentize from 'segmentize'

import 'style!css!react-pagify/style.css'

import 'style!css!reactabular/style.css'

export default React.createClass({
    displayName: 'PreviewsGrid'
  , propTypes: {
      issueNumber: React.PropTypes.number
  }
  , getInitialState() {
      return {
        gridData: []
      , pagination: {
          page: 1,
          perPage: 25
        }
      }
  }
  , componentWillMount() {
      PreviewsStore.addChangeListener(this.previewsStoreUpdate)
  }
  , componentWillReceiveProps(nextProps) {
      if (nextProps.issueNumber > 0 && this.props.issueNumber != nextProps.issueNumber) {
        getIssue(nextProps.issueNumber)
      }
  }
  , previewsStoreUpdate() {
      const data = PreviewsStore.getIssue(this.props.issueNumber)
      this.setState({
        gridData: data
      })
  }
  , onSelect(page) {
    var pagination = this.state.pagination || {};
    pagination.page = page;

    this.setState({
        pagination: pagination
    });
  }
  , render() {
      const columns = [
        {
            property: 'id'
          , header: "Previews Code"
        }
      , {
            property: 'title'
          , header: 'Description'
        }
      , {
            property: 'price'
          , header: 'Price'
        }
      , {
            property: 'listPrice'
          , header: 'Was'
        }
      , {
            property: 'publisher'
          , header: 'Publisher'
        }
      ]
      let pagination = this.state.pagination
      const currentPage = this.state.pagination.page
      const paginated = paginate(this.state.gridData, pagination)
      const pages = Math.ceil(this.state.gridData.length / Math.max(
        isNaN(pagination.perPage) ? 1 : pagination.perPage, 1)
      );

      return(
        <div>
          <Paginator.Context className="pagify-pagination"
            segments={segmentize({
              page: pagination.page,
              pages: pages,
              beginPages: 1,
              endPages: 1,
              sidePages: 2
            })} onSelect={this.onSelect} ellipsis={'…'}>
            <Paginator.Button page={currentPage - 1}>Previous</Paginator.Button>
            <Paginator.Segment field="beginPages" />
              <Paginator.Ellipsis
                className="ellipsis"
                previousField="beginPages"
                nextField="previousPages">
                ***
            </Paginator.Ellipsis>

            <Paginator.Segment field="previousPages" />
            <Paginator.Segment field="centerPage" className="selected" />
            <Paginator.Segment field="nextPages" />

            <Paginator.Ellipsis
              className="ellipsis"
              previousField="nextPages"
              nextField="endPages">
              ***
            </Paginator.Ellipsis>
            <Paginator.Segment field="endPages" />
            <Paginator.Button page={currentPage + 1}>Next</Paginator.Button>
          </Paginator.Context>
          <Table
            data={paginated.data}
            columns={columns}
          />
        </div>
      )
  }
})

function paginate(data, o) {
  data = data || [];

  // adapt to zero indexed logic
  const page = o.page - 1 || 0;
  const perPage = o.perPage;

  const amountOfPages = Math.ceil(data.length / perPage);
  const startPage = page < amountOfPages ? page: 0;

  return {
    amount: amountOfPages,
    data: data.slice(startPage * perPage, startPage * perPage + perPage),
    page: startPage
  };
}
