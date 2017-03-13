import React, { PropTypes } from 'react';
import Layout from '../../components/Layout';
import UploadHOC from '../../components/Uploader';
import UploadBox from '../../components/UploadBox';
import s from './styles.css';
import { title, html } from './index.md';
import {acceptedAudioMimeTypes} from '../config';
// import ReconnectingWebsocket from 'reconnectingwebsocket';


class HomePage extends React.Component {

  static propTypes = {
    articles: PropTypes.arrayOf(PropTypes.shape({
      url: PropTypes.string.isRequired,
      title: PropTypes.string.isRequired,
      author: PropTypes.string.isRequired,
    }).isRequired).isRequired,
  };
  constructor() {
    super();
    this.sendMessage = this.sendMessage.bind(this);
    this.recieveMessage = this.recieveMessage.bind(this);
  }
  sendMessage() {
    this.chat_socket.send(JSON.stringify({message: 'Hello World'}));
  }
  recieveMessage(message) {
    console.log('message', message);
  }
  componentDidMount() {
    document.title = title;
    //todo : connect to socket
    const ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";

    this.chat_socket = new WebSocket(ws_scheme + '://' + 'localhost:8000' + "/");
    this.chat_socket.onmessage = this.recieveMessage;
    // const chat_socket = new ReconnectingWebsocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);

  }

  render() {
    const Uploader = UploadHOC(UploadBox, '/upload', acceptedAudioMimeTypes );

    return (
      <Layout className={s.content}>
        <Uploader />
        <button onClick={this.sendMessage}> Send Message test </button>
      </Layout>
    );
  }

}

export default HomePage;
