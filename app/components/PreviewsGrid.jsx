import React from 'react'
import {getIssue} from '../actions/PreviewsActions'
import PreviewsStore from '../stores/PreviewsStore'
import PreviewsLink from './PreviewsLink'
import {Table, Search} from 'reactabular'
import Paginator from 'react-pagify'
import segmentize from 'segmentize'
import R from 'ramda'

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
      , search: {
          column: '',
          query: ''
        }
      }
  }
  , componentWillMount() {
      PreviewsStore.addChangeListener(this.previewsStoreUpdate)
  }
  , previewsStoreUpdate() {
      const data = PreviewsStore.getIssue()
      this.setState({
        gridData: data
      })
  }
  , onSelect(page) {
      const state = this.state;
      const pagination = state.pagination || {};
      const pages = Math.ceil(state.gridData.length / pagination.perPage);

      pagination.page = Math.min(Math.max(page, 1), pages);

      this.setState({
        pagination: pagination
      });
  }
  , onSearch(search) {
    this.setState({
        search: search
    });
  }
  , render() {
      const columns = [
        {
            property: 'id'
          , header: "Previews Code"
          , cell: (v) => {
              return {
                value: <PreviewsLink previewsCode={v} />
              }
            }
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
      const searchColumns = R.filter(R.where({property: R.contains(R.__, ['title', 'publisher'])}))(columns)
      let pagination = this.state.pagination
      let data = this.state.gridData
      const currentPage = pagination.page
      const pages = Math.ceil(data.length / Math.max(
        isNaN(pagination.perPage) ? 1 : pagination.perPage, 1)
      )

      if (this.state.search.query) {
        data = Search.search(
            data,
            columns,
            this.state.search.column,
            this.state.search.query
        )
      }
      const paginated = paginate(data, pagination)

      return(
        <div>
          <div className='search-container'>
            Search <Search columns={searchColumns} data={this.state.gridData} onChange={this.onSearch} />
          </div>
          <Table
            data={paginated.data}
            columns={columns}
            rowKey={'id'}
          />
        <Paginator.Context className="pagify-pagination"
            segments={segmentize({
              page: pagination.page,
              pages: pages,
              beginPages: 1,
              endPages: 1,
              sidePages: 2
            })} onSelect={this.onSelect}>
            <Paginator.Button page={currentPage - 1}>Previous</Paginator.Button>
            <Paginator.Button page={currentPage + 1}>Next</Paginator.Button>
          </Paginator.Context>
        </div>
      )
  }
})

function paginate(data, o) {
  data = data || [];

  console.log(o)
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
