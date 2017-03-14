import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import Layout from '../../components/Layout';
import s from './styles.css';
import { title, html } from './index.md';

import * as speechActions from '../../actions/speech';
import ReconnectingWebsocket from 'reconnectingwebsocket';

@connect(state => ({
  // runtimeVariableSet: state.speech.runtimeVariableSet
  transcriptions: state.speech.transcriptions,
  tones: state.speech.tones
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
    const {loadTranscription, loadSentenceTone, loadDocumentTone, endAnalysis} = this.props;
    let data = {};
    console.log(message.data);
    try {
      data = JSON.parse(message.data);
    } catch(e) {
      if (e instanceof SyntaxError) {
        //todo: dispatch errors
        console.log('syntax error..', e);
      }
      else {
        console.log('some unknown error', e);
      }
      return null;
    }

    switch(data.type) {
      case 'loadTranscription':
        loadTranscription(data);
        break;
      case 'loadSentenceTone':
        loadSentenceTone(data);
        break;
      case 'loadDocumentTone':
        loadDocumentTone(data);

      // case 'analysisComplete':
      //   endAnalysis();
        break;
      default:
        return null;
    }
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


    return (
      <Layout className={s.content}>

        {/*<button onClick={this.sendMessage}> Send Message test </button>*/}
      </Layout>
    );
  }

}

export default HomePage;
