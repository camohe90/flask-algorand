// static/script.js
function clearMessage() {
  setTimeout(function() {
    console.log("Acá vamos")
      var messageElement = document.getElementById("message");
      if (messageElement) {
          messageElement.remove();
      }
  }, 3000); // Remove message after 3 seconds (adjust as needed)
}
