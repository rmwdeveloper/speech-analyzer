import {


} from '../constants';

const initialState = {
  showSpaceIndicator: false,
  // uploads: {}
};

export default function storage(state = initialState, action) {
  const newUploads = { ...state.uploads };
  switch (action.type) {
    case CHECK_AVAILABLE_SPACE:
      return { ...state, showSpaceIndicator: true };
    case UPLOAD_START:
      newUploads[action.temporaryUploadId] = {progress: 0};
      return {...state, uploads: newUploads };
    // case UPLOAD_PROGRESS:
    //   newUploads[action.temporaryUploadId].progress = action.progress;
    //   return {...state, uploads: newUploads };
    case UPLOAD_COMPLETE:
      return { ...state, showSpaceIndicator: false };
    default:
      return state;
  }
}
