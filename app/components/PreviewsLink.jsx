import React from 'react';
const MonthNames = [
    'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC',
];

export default React.createClass({
  displayName: 'PreviewsLink',

  propTypes: {
    previewsCode: React.PropTypes.string,
  },

  componentWillMount() {
    const components = this.props.previewsCode.split('/');
    const issueNumber = +components[0];
    const epoch = new Date(1988, 8, 1);
    epoch.setMonth(epoch.getMonth() + issueNumber);
    const slug = MonthNames[epoch.getMonth()] + (epoch.getFullYear() - 2000) + components[1];

    this.setState({
        url: `http://www.previewsworld.com/Catalog/${slug}`,
      });
  },

  render() {
    return <a href={this.state.url}>{this.props.previewsCode}</a>;
  },
});
