import React from 'react';

const MonthNames = [
  'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
];

const codeToUrl = (previewsCode) => {
  const components = previewsCode.split('/');
  const issueNumber = +components[0];
  const epoch = new Date(1988, 8, 1);

  epoch.setMonth(epoch.getMonth() + issueNumber);
  const slug = MonthNames[epoch.getMonth()] + (epoch.getFullYear() - 2000) + components[1];

  return `http://www.previewsworld.com/Catalog/${slug}`;
};

const PreviewsLink = ({ previewsCode }) => (
  <a href={codeToUrl(previewsCode)}>{previewsCode}</a>
);

PreviewsLink.propTypes = {
  previewsCode: React.PropTypes.string
};

export default PreviewsLink;
