import React from 'react';
import PreviewsLink from './PreviewsLink';
import { Table, Search } from 'reactabular';
import Paginator from 'react-pagify';
import segmentize from 'segmentize';
import R from 'ramda';

import 'style!css!react-pagify/style.css'; // eslint-disable-line
import 'style!css!reactabular/style.css'; // eslint-disable-line

const firstLowerCaseLetter = /(^|[^a-zA-Z\u00C0-\u017F'])([a-zA-Z\u00C0-\u017F])/g;
const capitalize = (s) => s.toLowerCase().replace(firstLowerCaseLetter, m => m.toUpperCase());

// Rather than being fancy about it, I'll just handle the small number of edge cases
// for acronyms in this context.
const titleFormat = (title) => (
  capitalize(title)
    .replace(/Dc /, 'DC ')
    .replace(/Idw /, 'IDW ')
    .replace(/ Tp ?/, ' TP ')
    .replace(/ Hc ?/, ' HC ')
);

const formatAsGBP = (v) => {
  const currency = (c) => c.toLocaleString(null, { style: 'currency', currency: 'GBP' });
  return {
    value: (v) ? `£${currency(v)}` : ''
  };
};

const columns = [
  {
    property: 'previewsCode',
    header: 'Previews Code',
    cell: (v) => ({ value: <PreviewsLink previewsCode={v} /> }),
  },
  {
    property: 'title',
    header: 'Description',
    cell: (v) => ({ value: v ? titleFormat(v) : '' })
  },
  {
    property: 'price',
    header: 'Price',
    cell: formatAsGBP,
  },
  {
    property: 'listPrice',
    header: 'Was',
    cell: formatAsGBP,
  },
  {
    property: 'publisher',
    header: 'Publisher',
    cell: (v) => ({ value: v ? titleFormat(v) : '' }),
  },
  {
    header: 'Include'
  },
];

function paginate(data = [], o) {
  const page = o.page - 1 || 0;
  const perPage = o.perPage;

  const amountOfPages = Math.ceil(data.length / perPage);
  const startPage = page < amountOfPages ? page : 0;

  return {
    amount: amountOfPages,
    data: data.slice(startPage * perPage, startPage * perPage + perPage),
    page: startPage,
  };
}

export default class PreviewsGrid extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      pagination: {
        page: 1,
        perPage: 25,
      },
      search: {
        column: '',
        query: '',
      },
    };

    this.onSearch = this.onSearch.bind(this);
    this.onSelect = this.onSelect.bind(this);
  }

  onSelect(page) {
    const state = this.state;
    const pagination = state.pagination || {};
    const pages = Math.ceil(this.props.gridData.length / pagination.perPage);

    pagination.page = Math.min(Math.max(page, 1), pages);

    this.setState({
      pagination,
    });
  }

  onSearch(search) {
    this.setState({
      search
    });
  }

  render() {
    let data = this.props.gridData;
    const pagination = this.state.pagination;
    const currentPage = pagination.page;
    const pages = Math.ceil(data.length / pagination.perPage);
    const searchColumnsFilter = R.filter(
      R.where({
        property: R.contains(R.__, this.props.searchableProperties)
      })
    );
    const searchColumns = searchColumnsFilter(columns);

    if (this.state.search.query) {
      data = Search.search(
          data,
          columns,
          this.state.search.column,
          this.state.search.query
      );
    }

    const paginated = paginate(data, pagination);

    return (
      <div>
        <div className="search-container">
          Search
          <Search
            columns={searchColumns}
            data={this.props.gridData}
            onChange={this.onSearch}
          />
        </div>
        <Table
          data={paginated.data}
          columns={columns}
          rowKey={'id'}
        />
        <Paginator.Context
          className="pagify-pagination"
          segments={segmentize({
            page: pagination.page,
            pages,
            beginPages: 1,
            endPages: 1,
            sidePages: 2,
          })}
          onSelect={this.onSelect}
        >
          <Paginator.Button page={currentPage - 1}>Previous</Paginator.Button>
          <Paginator.Button page={currentPage + 1}>Next</Paginator.Button>
        </Paginator.Context>
      </div>
      );
  }
}

PreviewsGrid.propTypes = {
  gridData: React.PropTypes.array,
  searchableProperties: React.PropTypes.array
};

