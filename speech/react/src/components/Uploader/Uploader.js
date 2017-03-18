import React, { PropTypes, Component } from 'react';
import uuidV4 from 'uuid/v4';
import Resumable from 'resumablejs';


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
      this.resumable = new Resumable({
        target: 'http://localhost:8000/upload/',
        testChunks: false,
      });
      this.resumable.on('fileAdded', (file) => {
        this.resumable.upload();
      });
      this.resumable.on('progress', () => {
        console.log(this.resumable.progress());

      });
      this.resumable.on('complete', () => {
        //todo: handle multiple uploads ..?

        const uploadId = this.resumable.files[0].uniqueIdentifier;
        const data = new FormData();
        data.append('uploadId', uploadId);
        fetch('http://localhost:8000/upload_complete/', {method: 'post',body:data }
        ).then(response => {
          }).catch(error => {
            this.props.error(error);
            console.log('error',error);
          })
      });
      this.resumable.assignBrowse(this.uploader);

      // this.dropzone = new Dropzone(this.uploader, {url: uploadUrl,
      //   autoProcessQueue:false,
      //   clickable: true,
      //   acceptedFiles: acceptedFiles.toString(),
      //   createImageThumbnails: false,
      //   previewsContainer: null,
      //   addedfile: file => {
      //
      //     const data = new FormData();
      //     data.append('audio', file);
      //     const uploadId = uuidV4();
      //     this.props.startAnalysis(uploadId);
      //     fetch('http://localhost:8000/upload/', {method: 'post', body: data } ).then(response => {
      //       response.json().then(body => {
      //         this.props.loadAudio({id: body.id, name: file.name, uploadId});
      //
      //       })
      //     }).catch(error => {
      //       this.props.error(error);
      //       console.log('error',error);
      //     })
      //
      //   }
      // });


      // this.uploader.addEventListener('click', this.test);
      // this.input.addEventListener('change', this.clickFile);

    }
    render() {
      const accepted = acceptedFiles.join('|');

      return (<div style={{display: 'inline-block'}} ref={(uploader) => { this.uploader = uploader; }}>
        <div accept={accepted} ref={(input) => { this.input = input; }} style={{display: 'none'}} type="file" />
        <WrappedComponent  {...this.props} />
      </div>);
    }
  }
}
