import React from 'react'

export default class PreviewsGrid extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    const msg = (this.props.selectedIssue)
                  ? "Selected issue is " + this.props.selectedIssue
                  : "No issue currently selected"

    return(<div>{msg}</div>)
  }
}
