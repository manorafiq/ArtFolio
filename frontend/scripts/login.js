// Login.js

document.addEventListener("DOMContentLoaded", () => {
  document
    .querySelector(".login_form")
    .addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      try {
        const response = await fetch("http://127.0.0.1:5000/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email, password }),
        });

        const data = await response.json();

        if (response.ok) {
          // Store user_id in LocalStorage or sessionStorage
          localStorage.setItem("user_id", data.user_id);
          window.location.href = "/dashboard.html";
        } else {
          alert(data.error);
        }
      } catch (error) {
        console.error("Error", error);
        alert("An error occurred. Please try again.");
      }
    });
});
