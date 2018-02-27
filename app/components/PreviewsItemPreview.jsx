import React from 'react';
import PropTypes from 'prop-types';

const codeToUrl = (previewsCode) => {
  const components = previewsCode.split('/');
  return `/api/previews/${components[0]}/${components[1]}`;
};

function checkStatus(resp) {
  if (resp.status === 200) return resp.json();

  return Promise.reject(new Error(resp.statusText));
}

class PreviewsItemPreview extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      previewsCode: this.props.previewsCode,
      description: undefined,
      creators: undefined,
      haveData: false
    };
  }

  componentDidMount() {
    const myHeaders = new Headers();
    const conf = {
      method: 'GET',
      headers: myHeaders,
      cache: 'default'
    };
    fetch(codeToUrl(this.state.previewsCode), conf)
      .then(checkStatus)
      .then((data) => {
        this.setState({
          creators: data.creators,
          description: data.description,
          coverImage: data.coverImage,
          haveData: true
        });
      })
      .catch((err) => { throw new Error(err); });
  }

  render() {
    if (!this.state.haveData) {
      return <b>Loading...</b>;
    }

    return (
      <div className="item_display">
        <div className="imagecontainer">
          <img
            alt="Cover"
            width="300px"
            height="395px"
            src={this.state.coverImage}
          />
        </div>
        <div className="item_details">
          <p className="creators">{this.state.creators}</p>
          <p
            className="description"
            dangerouslySetInnerHTML={{ __html: this.state.description}} //eslint-disable-line
          />
        </div>
      </div>
    );
  }
}

PreviewsItemPreview.propTypes = {
  previewsCode: PropTypes.string.isRequired
};

export default PreviewsItemPreview;
