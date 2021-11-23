var videoWidth = 320;
var videoHeight = 240;
var videoTag = document.getElementById('theVideo');
var canvasTag = document.getElementById('theCanvas');
var csrf = document.getElementsByName("csrfmiddlewaretoken")
var msg = document.getElementById("message")

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
    $.ajax({
      type: 'POST',
      url: '',
      data: {
        imagen: data,
        letra: e.key
      },
      dataType: 'json',
      success: function (response) {
        document.getElementById("message").innerHTML = response.msg
        document.getElementById("estado").innerHTML = response.estado
      }
    })
  };
};