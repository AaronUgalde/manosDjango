var videoWidth = 320;
var videoHeight = 240;
var videoTag = document.getElementById('theVideo');
var canvasTag = document.getElementById('theCanvas');
var btnCapture = document.getElementById("btnCapture");
var btnDownloadImage = document.getElementById("btnDownloadImage");
videoTag.setAttribute('width', videoWidth);
videoTag.setAttribute('height', videoHeight);
canvasTag.setAttribute('width', videoWidth);
canvasTag.setAttribute('height', videoHeight);
window.onload = () => {
  navigator.mediaDevices.getUserMedia({
  audio: false,
  video: {
    width: videoWidth,
    height: videoHeight
  }}).then(stream => {
    videoTag.srcObject = stream;
  }).catch(e => {
    document.getElementById('errorTxt').innerHTML = 'ERROR: ' + e.toString();
  });
  var canvasContext = canvasTag.getContext('2d');
  window.onkeydown =  (e) => {
    canvasContext.drawImage(videoTag, 0, 0, videoWidth, videoHeight);
    var data = canvasTag.toDataURL("image/png")
    console.log("presionada: "+e.key)
    document.getElementById("imagen").value = data 
    document.getElementById("letra").value = e.key
    document.formulario.submit()
  };
};