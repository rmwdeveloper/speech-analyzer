import {
  LOAD_TRANSCRIPTION,
  LOAD_TONE,
  LOAD_AUDIO
} from '../constants';

const initialState = {
  audios: {},
  transcriptions: {}, // {id: {transcription: '', confidence: 0.3} }
  tones: {}
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
    default:
      return state;
  }
}
