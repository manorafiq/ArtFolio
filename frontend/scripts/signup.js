document.addEventListener("DOMContentLoaded", () => {
  document
    .querySelector(".signup_form")
    .addEventListener("submit", async (e) => {
      e.preventDefault();
      const fullName = document.getElementById("name").value;
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      const profession = document.getElementById("profession").value;

      try {
        const response = await fetch("http://127.0.0.1:5000/signup", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            ful_name: fullName,
            email,
            password,
            profession,
          }),
        });

        const data = await response.json();

        if (response.ok) {
          alert("Signup successful! Please log in.");
          window.location.href = "/login.html";
        } else {
          alert(data.error);
        }
      } catch (error) {
        console.error("Error:", error);
        alert("An error occurred. Please try again");
      }
    });
});
