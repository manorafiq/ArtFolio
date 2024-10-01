async function fetchProjects() {
  try {
    const response = await fetch("/api/projects");
    const projects = await response.json();
    displayProjects(projects);
  } catch (error) {
    console.error("Error fetching projects:", error);
    alert("Failed to load projects. Please try again.", error);
  }
}

function dispalyProjects(projects) {
  const projectsContainer = document.getElementById("projects-container");
  projectsContainer.innerHTML = "";

  projects.forEach((project) => {
    const projectElement = document.createElement("div");
    projectElement.className = "project";
    projectElement.innerHTML = `
      <div class="thumbnail">
        <img src="${project.thumbnail}" alt="${project.title}">
      </div>
      <div class="info">
      <h3>${project.title}</h3>
      <p>${project.description}</p>
    </div>
    `;

    projectsContainer.appendChild(projectElement);
  });
}

// Call this function when the page Loads
document.addEventListener('DOMContentLoaded', fetchProjects);

// const projects = [
//   {
//     id: 1,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 2,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 3,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 4,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 5,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 6,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 7,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 8,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 9,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 10,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 11,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 12,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 13,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 14,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 15,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
//   {
//     id: 16,
//     thumbnail: "./assets/background_image.jpg",
//     user_name: "John Doe",
//     title: "Nature's Post dried fruits",
//   },
// ];

// projects.map((project) => {

// })
