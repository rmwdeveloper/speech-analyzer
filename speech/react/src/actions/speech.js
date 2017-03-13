// import fetch from '../core/fetch';
import {
  SET_RUNTIME_VARIABLE
} from '../constants';

export function setRuntimeVariable() {
  return dispatch => {
    dispatch({ type: SET_RUNTIME_VARIABLE });
  };
}

