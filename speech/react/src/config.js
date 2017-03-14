export const acceptedAudioMimeTypes = ['video/*', 'audio/*'];
export const baseURL = 'http://localhost:8000';
export const baseAPI = 'speech/api/v1/';

export const audioAPI = `${baseURL}/${baseAPI}audio`;
export const transcriptionAPI = `${baseURL}/${baseAPI}transcription`;
export const documentToneAPI = `${baseURL}/${baseAPI}document_tone`;
export const sentenceToneAPI = `${baseURL}/${baseAPI}sentence_tone`;
