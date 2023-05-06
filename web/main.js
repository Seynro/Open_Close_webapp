const activateButton = document.getElementById("activate-button");
const animatedButton = document.getElementById("animated-button");

activateButton.addEventListener("click", function() {
  animatedButton.classList.add("animated");
});