/* jshint esversion: 11 */

/**
 * -- ALL PAGES WITH CONTACT BUTTON IN NAV --
 * Handles contact form submission.
 * Prevents page reload and sends data asynchronously.
 * Displays success/error messages dynamically.
 */
document.addEventListener("DOMContentLoaded", function () {
  const contactForm = document.getElementById("contact-form");
  const responseDiv = document.getElementById("contact-response");

   function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  const csrftoken = getCookie("csrftoken");

  contactForm.addEventListener("submit", function (e) {
    e.preventDefault(); // prevent page reload

    const formData = new FormData(contactForm);

    fetch(contactForm.action, {
      method: "POST",
      body: formData,
      headers: {
       "x-requested-with": "XMLHttpRequest",
        "X-CSRFToken": csrftoken,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.success) {
          responseDiv.innerHTML = `<div class="alert alert-custom-success">${data.message}</div>`;
          contactForm.reset(); // clear form if desired
        } else {
          responseDiv.innerHTML = `<div class="alert alert-danger">Something went wrong. Please try again.</div>`;
        }
      })
      .catch(() => {
        responseDiv.innerHTML = `<div class="alert alert-danger">Error sending message.</div>`;
      });
  });
});

/**
 * -- ALL PAGES --
 * Function to clear newsletter input field (in footer) after closing 
 * success modal. Runs code after the DOM is fully loaded
 */ 
document.addEventListener('DOMContentLoaded', function () {

  // Get subscription modal element
  var subModal = document.getElementById('sub-modal');

  // Clear newsletter input field after closing modal
  subModal.addEventListener('hidden.bs.modal', function () {
    var el = document.getElementById('newsletter');
    if (el) el.value = '';
  });
});

