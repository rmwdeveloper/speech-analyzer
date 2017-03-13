import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import Layout from '../../components/Layout';
import UploadHOC from '../../components/Uploader';
import UploadBox from '../../components/UploadBox';
import s from './styles.css';
import { title, html } from './index.md';
import {acceptedAudioMimeTypes} from '../../config';
import * as speechActions from '../../actions/speech';
import ReconnectingWebsocket from 'reconnectingwebsocket';

@connect(state => ({
  runtimeVariableSet: state.speech.runtimeVariableSet
}), { ...speechActions })
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
    this.recieveMessage = this.recieveMessage.bind(this);
  }

  recieveMessage(message) {
    console.log(message.data);
  }
  componentDidMount() {
    document.title = title;
    //todo : connect to socket
    const ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";

    this.chat_socket = new ReconnectingWebsocket(ws_scheme + '://' + 'localhost:8000' + "/");
    this.chat_socket.onmessage = this.recieveMessage;
    // const chat_socket = new ReconnectingWebsocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);

  }

  render() {
    const Uploader = UploadHOC(UploadBox, '/upload', acceptedAudioMimeTypes );

    return (
      <Layout className={s.content}>
        <Uploader />
        {/*<button onClick={this.sendMessage}> Send Message test </button>*/}
      </Layout>
    );
  }

}

export default HomePage;
