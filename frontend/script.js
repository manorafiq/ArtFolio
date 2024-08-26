document.addEventListener("DOMContentLoaded", () => {
    const imageContainer = document.querySelectorAll(".image");
    const heroContainer = document.querySelectorAll(".hero_contianer");
    
    imageContainer.forEach((heading) => {
        
    })
});

// document.addEventListener("DOMContentLoaded", () => {
//     const imageContainers = document.querySelectorAll(".image");

//     imageContainers.forEach((container) => {
//       let currentIndex = 0;
//       const images = container.querySelectorAll("img");

//       // Hide all images except the first one
//       images.forEach((img, index) => {
//         img.style.opacity = index === 0 ? "1" : "0";
//         img.style.position = "absolute"; // Stack images on top of each other
//       });

//       // Function to cycle through the images
//       function showNextImage() {
//         images[currentIndex].style.opacity = "0"; // Hide the current image
//         currentIndex = (currentIndex + 1) % images.length; // Move to the next image
//         images[currentIndex].style.opacity = "1"; // Show the next image
//       }

//       // Run the cycle every 3 seconds
//       setInterval(showNextImage, 3000);
//     });
//   });

// document.addEventListener("DOMContentLoaded", () => {
//   const imageContainers = document.querySelectorAll(".images .image");

//   let currentIndex = 0;

//   function showNextImage() {
//     // Hide all images first
//     imageContainers.forEach((container, index) => {
//       container.style.opacity = "0";
//       container.style.zIndex = index === currentIndex ? "2" : "1";
//     });

//     // Show the current image container
//     const currentContainer = imageContainers[currentIndex];
//     currentContainer.style.opacity = "1";
//     currentContainer.style.animation = "slideInFromBottom 1s ease-in forwards, slideOutToTop 1s 10s ease-in forwards";

//     // Move to the next container
//     currentIndex = (currentIndex + 1) % imageContainers.length;

//     // Run the transition every 12 seconds
//     setInterval(showNextImage, 12000);

//     // Start the frist transition immediately
//     showNextImage();
//   }
// });
