import {
  SET_RUNTIME_VARIABLE
} from '../constants';

const initialState = {
  runTimeVariableSet: false,
  // uploads: {}
};

export default function speech(state = initialState, action) {
  switch (action.type) {
    case SET_RUNTIME_VARIABLE:
      return {...state, runTimeVariableSet: true};
    default:
      return state;
  }
}
