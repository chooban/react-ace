import React from 'react'
import {getIssue} from '../actions/PreviewsActions'
import PreviewsStore from '../stores/PreviewsStore'
import {Table} from 'reactabular'

import 'style!css!reactabular/style.css'

export default React.createClass({
    displayName: 'PreviewsGrid'
  , propTypes: {
      issueNumber: React.PropTypes.number
  }
  , getInitialState() {
      return {
        gridData: []
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
      return(
        <Table
          data={this.state.gridData}
          columns={columns}
        />
      )
  }
})
