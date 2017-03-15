export const acceptedAudioMimeTypes = ['video/*', 'audio/*'];
export const baseURL = 'localhost:8000'; // todo: change to basedomain
export const baseAPI = 'speech/api/v1/';
export const scheme = window.location.protocol;

export const audioAPI = `${scheme}//${baseURL}/${baseAPI}audio/`;
export const transcriptionAPI = `${scheme}//${baseURL}/${baseAPI}transcription/`;
export const documentToneAPI = `${scheme}//${baseURL}/${baseAPI}document_tone/`;
export const sentenceToneAPI = `${scheme}//${baseURL}/${baseAPI}sentence_tone/`;
