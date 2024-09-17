document.addEventListener("DOMContentLoaded", () => {
    const dynamicImage = document.getElementById("dynamicImage");
    const mainContent = document.querySelector(".main-content");
    const body = document.querySelector("body");
  
    dynamicImage.addEventListener("animationend", () => {
      // After the image has flashed, blurred, and moved, hide it
      dynamicImage.style.display = "none";
      
      // Show the main content and activate the background blur
      mainContent.style.display = "block";
      body.classList.add("bg-active");
    });
  });
  