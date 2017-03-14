// import fetch from '../core/fetch';
import {
  SET_RUNTIME_VARIABLE,
  LOAD_TRANSCRIPTION,
  LOAD_TONE,
  LOAD_AUDIO,
  START_ANALYSIS,
  END_ANALYSIS
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

export function loadTone(data) {
  const { toneName, score, categoryName, transcription } = data;
  return dispatch => {
    dispatch({ type: LOAD_TRANSCRIPTION, toneName, score, categoryName, transcription });
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
