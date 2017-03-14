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

const initialState = {
  audios: {},
  transcriptions: {}, // {id: {transcription: '', confidence: 0.3} }
  sentenceTones: {},
  documentTones: {},
  errors: {}
  // uploads: {}
};

export default function speech(state = initialState, action) {
  const newTranscriptions = { ...state.transcriptions };
  const newAudios = { ...state.audios };
  const newSentenceTones = { ...state.sentenceTones };
  const newDocumentTones = { ...state.documentTones };
  switch (action.type) {
    case LOAD_AUDIO:
      newAudios[action.uploadId] = {filename: action.name, id: action.id};
      return {...state, audios: newAudios};
    case LOAD_TRANSCRIPTION:
      newTranscriptions[action.id] = { transcription:action.transcription, confidence: action.confidence,
      relation: action.relation};
      return {...state, transcriptions: newTranscriptions};
    case LOAD_SENTENCE_TONE:
      if (newSentenceTones.hasOwnProperty(action.relation)) {
      newSentenceTones[action.relation] = [...newSentenceTones[action.relation],
        {categoryName: action.categoryName, score: action.score, toneName: action.toneName,} ];
      } else {
        newSentenceTones[action.relation] = [
        {categoryName: action.categoryName, score: action.score, toneName: action.toneName,} ];
      }

      return {...state, sentenceTones: newSentenceTones};
    case LOAD_DOCUMENT_TONE:
      if (newDocumentTones.hasOwnProperty(action.relation)) {
      newDocumentTones[action.relation] = [...newDocumentTones[action.relation],
        {categoryName: action.categoryName, score: action.score, toneName: action.toneName,} ];
      } else {
        newDocumentTones[action.relation] = [
        {categoryName: action.categoryName, score: action.score, toneName: action.toneName,} ];
      }

      return {...state, sentenceTones: newSentenceTones};
    case START_ANALYSIS:
      newAudios[action.uploadId] = {filename: action.name};
      return { ...state, audios: newAudios};
    case END_ANALYSIS:
      return state;
    default:
      return state;
  }
}
