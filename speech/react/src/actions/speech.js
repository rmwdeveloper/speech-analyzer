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

export function loadTranscription(data) {
  const { transcription, confidence, id } = data;
  return dispatch => {
    dispatch({ type: LOAD_TRANSCRIPTION, transcription, confidence, id });
  };
}

export function loadDocumentTone(data) {
  const { toneName, score, categoryName, relation } = data;
  return dispatch => {
    dispatch({ type: LOAD_DOCUMENT_TONE, toneName, score, categoryName, relation });
  };
}

export function loadSentenceTone(data) {
  const { toneName, score, categoryName, relation } = data;
  return dispatch => {
    dispatch({ type: LOAD_SENTENCE_TONE, toneName, score, categoryName, relation });
  };
}

export function loadAudio(data) {
  const { name, id } = data;
  return dispatch => {
    dispatch({ type: LOAD_AUDIO, name, id });
  };
}

export function startAnalysis() {
  return dispatch => {
    dispatch({ type: START_ANALYSIS});
  };
}

export function endAnalysis() {
  return dispatch => {
    dispatch({ type: END_ANALYSIS});
  };
}

export function error(error) {
  return dispatch => {
    dispatch({ type: ERROR, error});
  };
}
