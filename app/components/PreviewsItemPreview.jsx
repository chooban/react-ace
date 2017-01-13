import React from 'react';

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
          haveData: true
        });
      })
      .catch((err) => { throw new Error(err); });
  }

  render() {
    return (
      <div>
        <p>{this.state.previewsCode}</p>
        {!this.state.haveData && <b>Loading...</b> }
        {this.state.haveData &&
          <div>
            <div className="creators">{this.state.creators}</div>
            <div className="description">{this.state.description}</div>
          </div>
        }
      </div>
    );
  }
}

PreviewsItemPreview.propTypes = {
  previewsCode: React.PropTypes.string
};

export default PreviewsItemPreview;
