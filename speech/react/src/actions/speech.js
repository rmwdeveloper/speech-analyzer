// import fetch from '../core/fetch';
import {audioAPI, transcriptionAPI, documentToneAPI, sentenceToneAPI} from '../config';
const forEach = require('async-foreach').forEach;


import {
  SET_RUNTIME_VARIABLE,
  LOAD_TRANSCRIPTION,
  LOAD_DOCUMENT_TONE,
  LOAD_SENTENCE_TONE,
  LOAD_AUDIO,
  START_ANALYSIS,
  END_ANALYSIS,
  ERROR,
  INITIALIZE
} from '../constants';



export function setRuntimeVariable() {
  return dispatch => {
    dispatch({ type: SET_RUNTIME_VARIABLE });
  };
}

/*
* Animate in a new "Analyzer Row", a div containing the filename, a loading icon,
* */
export function startAnalysis(uploadId) {
  return dispatch => {
    dispatch({ type: START_ANALYSIS, uploadId});
  };
}

/*
* Update the row with the transcriptions.
* */
export function loadTranscription({ transcription, confidence, id, relation }) {
  return dispatch => {
    dispatch({ type: LOAD_TRANSCRIPTION, transcription, confidence, id, relation });
  };
}


/*
* Color each sentence with color score?
* */

export function loadSentenceTone(data) {
  const { toneName, score, categoryName, relation } = data;
  return dispatch => {
    dispatch({ type: LOAD_SENTENCE_TONE, toneName, score, categoryName, relation });
  };
}

/*
* Add some kind of graph tab or something
* */
export function loadDocumentTone(data) {
  const { toneName, score, categoryName, relation } = data;
  return dispatch => {
    dispatch({ type: LOAD_DOCUMENT_TONE, toneName, score, categoryName, relation });
  };
}

/*
* Complete..
* */
export function loadAudio({ name, id, uploadId }) {

  return dispatch => {
    dispatch({ type: LOAD_AUDIO, name, id, uploadId });
  };
}

// todo: delete endAnalysis? loadAudio essentially performs the same funciton.
export function endAnalysis({}) {
  return dispatch => {
    dispatch({ type: END_ANALYSIS});
  };
}

export function error(error) {
  return dispatch => {
    dispatch({ type: ERROR, error});
  };
}


export function initialize() {
  return dispatch => {
    const headers = new Headers(); // todo: abstract away into own module
    headers.append('Content-Type', 'application/json');

    const response = fetch(audioAPI, {
      method: 'get', headers
    }).then(response => {
      response.json().then(audioBody => {
        forEach(audioBody, (data) => {
            dispatch({ type: LOAD_AUDIO, name: data.audio.substring(data.audio.lastIndexOf('/')+1) , id: data.id,
              uploadId: data.id });
          forEach(data.transcriptions, (transcription) => {
              fetch(transcription, {method:'get', headers}).then(transcriptionResponse=> {
              transcriptionResponse.json().then(transcriptionBody=> {
                const { transcription, confidence, id, audio} = transcriptionBody;
                 dispatch({ type: LOAD_TRANSCRIPTION, transcription, confidence, id, relation: audio });
                    transcriptionBody.sentence_tones.forEach(sentence_tone => {
                  const { id, score, toneName, categoryName } = sentence_tone;
                  dispatch({ type: LOAD_SENTENCE_TONE, id, toneName, score, categoryName, relation: transcriptionBody.id });
                });
              })
            })
          });
          // forEach(data.documument_tones, (document_tone) => {
          //   const { id, score, toneName, categoryName } = document_tone;
          //   dispatch({ type: LOAD_DOCUMENT_TONE, id, toneName, score, categoryName, relation: data.id });
          // });
        });
        // audioBody.forEach(data => {
        //
        //   dispatch({ type: LOAD_AUDIO, name: data.audio.substring(data.audio.lastIndexOf('/')+1) , id: data.id,
        //     uploadId: data.id });

          // data.transcriptions.forEach(transcription => {
          //   fetch(transcription, {method:'get', headers}).then(transcriptionResponse=> {
          //     transcriptionResponse.json().then(transcriptionBody=> {
          //       const { transcription, confidence, id, audio} = transcriptionBody;
          //        dispatch({ type: LOAD_TRANSCRIPTION, transcription, confidence, id, relation: audio });
          //       transcriptionBody.sentence_tones.forEach(sentence_tone => {
          //         const { id, score, toneName, categoryName } = sentence_tone;
          //         dispatch({ type: LOAD_SENTENCE_TONE, id, toneName, score, categoryName, relation: transcriptionBody.id });
          //       });
          //     })
          //   })
          // });

          // data.document_tones.forEach(document_tone => {
          //   const { id, score, toneName, categoryName } = document_tone;
          //   dispatch({ type: LOAD_DOCUMENT_TONE, id, toneName, score, categoryName, relation: data.id });
          // });
        // })

      }).catch(error => {
        console.log(error);
        dispatch({ type: ERROR, error});
      })
    }).catch(error => {
      dispatch({ type: ERROR, error});
    })
  };
}
