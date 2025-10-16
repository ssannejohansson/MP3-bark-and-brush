
    document.addEventListener('DOMContentLoaded', function () {
  var subModal = document.getElementById('sub-modal');
  subModal.addEventListener('hidden.bs.modal', function () {
    var el = document.getElementById('newsletter');
    if (el) el.value = '';
  });
});


(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()


  document.addEventListener('DOMContentLoaded', function () {
    const dayInput = document.getElementById('id_day');
    const timeSelect = document.getElementById('id_time');

    // 1. Get fully booked dates from backend
    fetch('/fully-booked-dates/')
      .then(res => res.json())
      .then(data => {
        const disabledDates = data.fully_booked_dates || [];

        // Initialize Flatpickr with disabled (fully booked) + weekends
        flatpickr("#id_day", {
          minDate: "today",
          dateFormat: "Y-m-d",
          disable: [
               ...disabledDates, // spread fully booked dates into the disable list
          function (date) {
            // Disable weekends: Sunday (0) and Saturday (6)
            return (date.getDay() === 0 || date.getDay() === 6);
    }
  ]
        });
      });

    // 2. Fetch available times when date is selected
    dayInput.addEventListener('change', function () {
      const selectedDate = this.value;

      if (!selectedDate) return;

      fetch(`/available-times/?day=${selectedDate}`)
        .then(response => response.json())
        .then(data => {
          const availableTimes = data.available_times || [];
          const allTimes = ["9:00 AM", "10:30 AM", "1:00 PM", "2:30 PM", "4:00 PM", "5:30 PM"];
          timeSelect.innerHTML = '';

          allTimes.forEach(time => {
            const option = document.createElement('option');
            option.value = time;
            option.textContent = time;

            if (!availableTimes.includes(time)) {
              option.disabled = true;
              option.style.color = '#aaa';  // gray out text
            }

            timeSelect.appendChild(option);
          });
        });
    });
  });


  document.addEventListener("DOMContentLoaded", function () {
  const contactForm = document.getElementById("contact-form");
  const responseDiv = document.getElementById("contact-response");

  contactForm.addEventListener("submit", function (e) {
    e.preventDefault(); // prevent page reload

    const formData = new FormData(contactForm);

    fetch(contactForm.action, {
      method: "POST",
      body: formData,
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.success) {
          responseDiv.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
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
