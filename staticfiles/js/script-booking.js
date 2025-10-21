/* jshint esversion: 11 */
/* global flatpickr */

/**
 * -- BOOKING PAGES -- 
 * Apply Bootstrap custom validation styles to forms
 */
(() => {
  'use strict';

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation');

  // Loop over them and prevent submission if form is invalid. 
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {

      // Stops submission if form inputs are invalid
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      // Apply Bootstraps "was validated" class to show feedback styles
      form.classList.add('was-validated');
    }, false);
  });
})();

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
        const allTimes = ["9:00 AM", "10:30 AM", "1:00 PM", "2:30 PM", "4:00 PM"];
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


/** 
 * -- BOOKING PAGES --
 * Alert messages will fade out after 2 seconds.
 */
document.addEventListener('DOMContentLoaded', function() {
  // Selects all alert messages
  const alerts = document.querySelectorAll('.alert');

  alerts.forEach(function(alert) {
    // Waits 2 seconds (2000 ms), then start fade out
    setTimeout(function() {
      alert.classList.add('fade-out');
      // Then remove it completely after animation ends 
      setTimeout(function() {
        alert.remove();
      }, 1000); // Matches CSS fade duration
    }, 2000);
  });
});


