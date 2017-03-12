import React, { PropTypes, Component } from 'react';

class Uploader extends Component {
  constructor() {
    super();
  }
  componentDidMount() {
    const { uploadUrl } = this.props;
    this.dropzone = new Dropzone(this.uploader, {url: 'uploadUrl',
      autoProcessQueue:false,
      clickable: true,
      createImageThumbnails: false,
      previewsContainer: null,
      addedfile: file => {
        console.log(file);
      }
    });

  }
  render() {
    console.log(this.props.children);
    return (<div style={{outline: '1px solid red', zIndex: 2}} ref={(uploader) => { this.uploader = uploader; }}>
      {this.props.children}
    </div>);
  }
}


export default Uploader;
