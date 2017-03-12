import React, { PropTypes, Component } from 'react';

class Uploader extends Component {
  constructor() {
    super();
  }
  componentDidMount() {
    const { uploadUrl } = this.props;
    this.dropzone = new Dropzone(this.uploader, {url: 'uploadUrl',
      autoProcessQueue:false,
      clickable: false,
      createImageThumbnails: false,
      previewsContainer: null,
      addedfile: file => {}
    });
  }
  render() {

    return (<div ref={(uploader) => { this.uploader = uploader; }}>
      {this.props.children}
    </div>);
  }
}


export default Uploader;
