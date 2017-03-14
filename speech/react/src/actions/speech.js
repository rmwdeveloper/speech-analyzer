// import fetch from '../core/fetch';
import {
  SET_RUNTIME_VARIABLE,
  LOAD_TRANSCRIPTION,
  LOAD_DOCUMENT_TONE,
  LOAD_SENTENCE_TONE,
  LOAD_AUDIO,
  START_ANALYSIS,
  END_ANALYSIS,
  ERROR
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
