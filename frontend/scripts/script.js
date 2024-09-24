document.addEventListener("DOMContentLoaded", () => {
  const heroTexts = document.querySelectorAll(".hero_text");
  const images = document.querySelectorAll(".images .image");
  let currentIndex = 0;
  const delay = 3000;

  const navBar = document.querySelector(".nav_bar");
  const searchBar = document.querySelector(".search_bar");
  const searchBarOffset = searchBar.offsetTop;

  window.addEventListener("scroll", () => {
    // Handle sticky navbar
    if (window.scrollY > 0) {
      navBar.classList.add("sticky");
    } else {
      navBar.classList.remove("sticky");
    }

    // Handle sticky search bar
    if (window.scrollY >= searchBarOffset - navBar.offsetHeight) {
      searchBar.classList.add("sticky");
    } else {
      searchBar.classList.remove("sticky");
    }
  });

  function cycleContent() {
    heroTexts[currentIndex].classList.remove("active");
    heroTexts[currentIndex].classList.add("disable");

    images[currentIndex].classList.remove("active");
    images[currentIndex].classList.add("disable");

    // Move to the next index, looping back to 0 if at the end
    currentIndex = (currentIndex + 1) % heroTexts.length;

    // Show the next hero text and image
    heroTexts[currentIndex].classList.add("active");
    heroTexts[currentIndex].classList.remove("disable");
    images[currentIndex].classList.add("active");
    images[currentIndex].classList.remove("disable");
  }

  // Initialize by showing the first hero text and image
  heroTexts[currentIndex].classList.add("active");
  heroTexts[currentIndex].classList.remove("disable");
  images[currentIndex].classList.add("active");
  images[currentIndex].classList.remove("disable");

  // Cycle the content every few seconds
  setInterval(cycleContent, delay);
});

/* Make Search bar Sticky */
// Sticky search bar functionality
// const searchBar = document.getElementById('search');
// const searchOffset = searchBar.offsetTop;

// window.addEventListener('scroll', () => {
//   if (window.pageYOffset >= searchOffset) {
//     searchBar.classList.add('sticky');
//   } else {
//     searchBar.classList.remove('sticky');
//   }
// });


window.onscroll = function () {
  makeSticky();
};
let search = document.getElementById("serach");

function makeSticky() {
  if (window.pageYOffset > 160) {
    search.classList.add("sticky");
  } else {
    search.classList.remove("sticky");
  }
}

// document.addEventListener("DOMContentLoaded", () => {
//     const heroTexts = document.querySelectorAll(".hero_text");
//     const images = document.querySelectorAll(".images img");
//     let currentIndex = 0;
//     const delay = 3000; // 3 seconds delay

//     function cycleContent() {
//       // Hide the current hero text and image
//       heroTexts[currentIndex].classList.remove("active");
//       images[currentIndex].classList.remove("active");

//       // Move to the next index, looping back to 0 if at the end
//       currentIndex = (currentIndex + 1) % heroTexts.length;

//       // Show the next hero text and image
//       heroTexts[currentIndex].classList.add("active");
//       images[currentIndex].classList.add("active");
//     }

//     // Initialize by showing the first hero text and image
//     heroTexts[currentIndex].classList.add("active");
//     images[currentIndex].classList.add("active");

//     // Cycle the content every few seconds
//     setInterval(cycleContent, delay);
//   });
