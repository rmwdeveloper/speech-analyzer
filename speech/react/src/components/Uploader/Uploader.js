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
        acceptedFiles: acceptedFiles.toString(),
        createImageThumbnails: false,
        previewsContainer: null,
        addedfile: file => {
          const data = new FormData();
          data.append('audio', file);

          fetch('http://localhost:8000/upload/', {method: 'post', body: data } ).then(response => {
            console.log(response);
            // response.json().then(body => {
            //   console.log(body);
            // })
          }).catch(error => {
            console.log('error',error);
          })

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
