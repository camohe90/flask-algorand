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

 // Pagination logic
 document.addEventListener("DOMContentLoaded", function () {
  var table = document.getElementById("dataTable");
  var tableRows = table.getElementsByTagName("tr");
  var totalPages = Math.ceil((tableRows.length - 1) / 10); // Assuming 10 rows per page
  var currentPage = 1;

  function showPage(page) {
      for (var i = 1; i < tableRows.length; i++) {
          if (i >= (page - 1) * 10 + 1 && i <= page * 10) {
              tableRows[i].style.display = "";
          } else {
              tableRows[i].style.display = "none";
          }
      }
  }

  function updatePagination() {
      var pagination = document.getElementById("pagination");
      pagination.innerHTML = "";
      var prevButton = document.createElement("button");
      prevButton.textContent = "Previous";
      prevButton.classList.add("btn"); 
      prevButton.addEventListener("click", function () {
          if (currentPage > 1) {
              currentPage--;
              showPage(currentPage);
          }
      });
      pagination.appendChild(prevButton);

      var nextButton = document.createElement("button");
      nextButton.textContent = "Next";
      nextButton.classList.add("btn"); 
      nextButton.addEventListener("click", function () {
          if (currentPage < totalPages) {
              currentPage++;
              showPage(currentPage);
          }
      });
      pagination.appendChild(nextButton);
  }

  showPage(currentPage);
  updatePagination();
});
