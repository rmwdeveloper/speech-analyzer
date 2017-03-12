import React, { PropTypes, Component } from 'react';

export default function uploader(WrappedComponent, uploadUrl, acceptedFiles) {
  return class extends Component {
    constructor(){
      super();
      this.test = this.test.bind(this);
      this.clickFile = this.clickFile.bind(this);

    }
    test() {
      this.input.click();
    }
    clickFile(event) {
      for( let iterator = 0; iterator < event.target.files.length; iterator++){
        this.dropzone.emit('addedfile', event.target.files[iterator]);
      }
    }
    componentDidMount() {

      this.dropzone = new Dropzone(this.uploader, {url: uploadUrl,
        autoProcessQueue:false,
        clickable: true,
        acceptedFiles,
        createImageThumbnails: false,
        previewsContainer: null,
        addedfile: file => {
          console.log(file);
        }
      });


      this.uploader.addEventListener('click', this.test);
      this.input.addEventListener('change', this.clickFile);

    }
    render() {
      const accepted = acceptedFiles.join('|');

      return (<div style={{display: 'inline-block'}} ref={(uploader) => { this.uploader = uploader; }}>
        <input accept={accepted} ref={(input) => { this.input = input; }} style={{display: 'none'}} type="file" />
        <WrappedComponent  {...this.props} />
      </div>);
    }
  }
}
