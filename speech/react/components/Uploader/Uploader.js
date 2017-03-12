import React, { PropTypes, Component } from 'react';

export default function uploader(WrappedComponent, uploadUrl) {
  return class extends Component {
    constructor(){
      super();
    }
    componentDidMount() {
      this.dropzone = new Dropzone(this.uploader, {url: '/',
        autoProcessQueue:false,
        createImageThumbnails: false,
        previewsContainer: null,
        addedfile: file => {
          console.log(file);
        }
      });
    }
    render() {
      return (<div style={{display: 'inline-block'}} ref={(uploader) => { this.uploader = uploader; }}>
        <WrappedComponent {...this.props} />
      </div>);
    }
  }
}
