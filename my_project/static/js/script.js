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

  // Listens for form submission and handle it asynchronously
  contactForm.addEventListener("submit", function (e) {
    e.preventDefault(); // Prevents page reload

    const formData = new FormData(contactForm);

    // Send form data via POST request using Fetch API
    fetch(contactForm.action, {
        method: "POST",
        body: formData,
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        },
      })
      .then((res) => res.json())
      .then((data) => {
        // Displays success or failure messages
        if (data.success) {
          responseDiv.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
          contactForm.reset(); // Clear form after successful submission
        } else {
          responseDiv.innerHTML = `<div class="alert alert-danger">Something went wrong. Please try again.</div>`;
        }
      })
      .catch(() => {
        // Handles network or server errors 
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



/**
 * -- BOOKING PAGES -- 
 * Apply Bootstrap custom validation styles to forms
 */
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission if form is invalid. 
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {

      // Stops submission if form inputs are invalid
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }
      // Apply Bootstraps "was validated" class to show feedback styles
      form.classList.add('was-validated')
    }, false)
  })
})()

/** 
 * -- BOOKING PAGES --
 * Initializes booking form functionality.
 * Disables fully booked and weekend dates using Flatpickr.
 * Dynamically loads available times when a date is selected.
 */
document.addEventListener('DOMContentLoaded', function () {
  const dayInput = document.getElementById('id_day');
  const timeSelect = document.getElementById('id_time');

  // 1. Gets fully booked dates from backend
  fetch('/fully-booked-dates/')
    .then(res => res.json())
    .then(data => {
      const disabledDates = data.fully_booked_dates || [];

      // Initializes Flatpickr with disabled (fully booked dates) and weekends
      flatpickr("#id_day", {
        minDate: "today",
        dateFormat: "Y-m-d",
        disable: [
          ...disabledDates, // Disables fully booked dates
          function (date) {
            // Disables weekends: Sunday (0) and Saturday (6)
            return (date.getDay() === 0 || date.getDay() === 6);
          }
        ]
      });
    });

  // 2. Fetches available times when date is selected
  dayInput.addEventListener('change', function () {
    const selectedDate = this.value;

    if (!selectedDate) return;

    fetch(`/available-times/?day=${selectedDate}`)
      .then(response => response.json())
      .then(data => {
        const availableTimes = data.available_times || [];
        const allTimes = ["9:00 AM", "10:30 AM", "1:00 PM", "2:30 PM", "4:00 PM", "5:30 PM"];
        timeSelect.innerHTML = '';

        // Sets dropdown to show available and unavailable times
        allTimes.forEach(time => {
          const option = document.createElement('option');
          option.value = time;
          option.textContent = time;

          // Disable and gray out unavailable times
          if (!availableTimes.includes(time)) {
            option.disabled = true;
            option.style.color = '#aaa'; 
          }

          timeSelect.appendChild(option);
        });
      });
  });
});
