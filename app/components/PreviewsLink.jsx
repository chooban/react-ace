import React from 'react'
import m from 'moment'

export default React.createClass({
    displayName: 'PreviewsLink'
  , propTypes: {
      previewsCode: React.PropTypes.string
  }
  , componentWillMount() {
      const components = this.props.previewsCode.split('/')
      const dateOfCatalogue = m('1988-9-01', 'YYYY-MM-DD').add(+components[0], 'months')
      const slug = dateOfCatalogue.format('MMMYY').toUpperCase() + components[1]

      this.setState({
        url: `http://www.previewsworld.com/Catalog/${slug}`
      })
  }
  , render() {
      return <a href={this.state.url}>{this.props.previewsCode}</a>
  }
})
