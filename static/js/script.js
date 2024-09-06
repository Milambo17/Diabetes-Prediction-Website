const modalContainer = document.querySelector(".modal-container");
const modals = modalContainer.querySelectorAll(".modal");
const readMoreBtns = modalContainer.querySelectorAll(".read-more");

readMoreBtns.forEach((btn, index) => {
  btn.addEventListener("click", () => {
    // Expand the modal
    modals[index].classList.add("expanded");

    // Make the expanded modal the main focus
    modals[index].classList.add("active");

    // Make the other modals less prominent
    for (let i = 0; i < modals.length; i++) {
      if (i !== index) {
        modals[i].classList.remove("active");
      }
    }
  });
});

function toggleSidebar() {
  var sidebar = document.getElementById("sidebar");
  var menuIcon = document.querySelector(".menu-icon");
  if (sidebar.style.width === "250px") {
    sidebar.style.width = "0";
    menuIcon.style.display = "block"; // Show the menu icon
  } else {
    sidebar.style.width = "250px";
    menuIcon.style.display = "none"; // Hide the menu icon
  }
}
document
  .getElementById("prediction-form")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form from submitting normally

    // Collect form data
    let formData = new FormData(this);
    let data = {};
    formData.forEach((value, key) => {
      data[key] = value;
    });

    // Send AJAX request
    fetch("/user_i", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        // Display the result
        let resultContainer = document.getElementById("result-container");
        resultContainer.style.display = "block";
        resultContainer.innerHTML = `<h2>Prediction Result: ${data.result}</h2>`;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
