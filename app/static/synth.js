const audioContext = new AudioContext();
const oscList = [];
let mainGainNode = null;

const keyboard = document.querySelector(".keyboard");
const wavePicker = document.querySelector("select[name='waveform']");
const volumeControl = document.querySelector("input[name='volume']");

let noteFreq = null;
let customWaveform = null;
let sineTerms = null;
let cosineTerms = null;

function test(){
  console.log('testing');
}