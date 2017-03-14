import {
  LOAD_TRANSCRIPTION,
  LOAD_DOCUMENT_TONE,
  LOAD_SENTENCE_TONE,
  LOAD_AUDIO,
  START_ANALYSIS,
  END_ANALYSIS
} from '../constants';

const initialState = {
  audios: {},
  transcriptions: {}, // {id: {transcription: '', confidence: 0.3} }
  tones: {},
  errors: {}
  // uploads: {}
};

export default function speech(state = initialState, action) {
  const newTranscriptions = { ...state.transcriptions };
  const newAudios = { ...state.audios };
  switch (action.type) {
    case LOAD_AUDIO:
      newAudios[action.id] = action.name;
      return {...state, audios: newAudios};
    case LOAD_TRANSCRIPTION:
      newTranscriptions[action.id] = { transcription:action.transcription, confidence: action.confidence };
      return {...state, transcriptions: newTranscriptions};
    case LOAD_DOCUMENT_TONE:
      return state;
    case LOAD_SENTENCE_TONE:
      return state;
    case START_ANALYSIS:
      return state;
    case END_ANALYSIS:
      return state;
    default:
      return state;
  }
}
