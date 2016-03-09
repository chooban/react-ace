import React from 'react'
import {getIssue} from '../actions/PreviewsActions'
import PreviewsStore from '../stores/PreviewsStore'
import DataGrid from 'react-datagrid'

import 'style!css!react-datagrid/index.css'

export default React.createClass({
    displayName: 'PreviewsGrid'
  , propTypes: {
      issueNumber: React.PropTypes.number
  }
  , getInitialState() {
      return {
        gridData: null
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
  , render() {
      var columns = [
        {
            name: 'id'
          , title: "Previews Code"
        }
      , {
            name: 'title'
          , title: 'Description'
        }
      , {
            name: 'price'
          , title: 'Price'
        }
      , {
            name: 'listPrice'
          , title: 'Was'
        }
      , {
            name: 'publisher'
          , title: 'Publisher'
        }
      ]
      return(
        <div>
          <p>This is the grid for {this.props.issueNumber}</p>
          <DataGrid
            idProperty="id"
            dataSource={this.state.gridData}
            columns={columns}
            pagination='true'
            pageSize='50'
          />
        </div>
      )
  }
})
