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

// Alert when successful contact input (change this later)
const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
const appendAlert = (message, type) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,,
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)
}

const alertTrigger = document.getElementById('liveAlertBtn')
if (alertTrigger) {
  alertTrigger.addEventListener('click', () => {
    appendAlert('Message successfully sent!', 'success')
  })
}


  document.addEventListener('DOMContentLoaded', function () {
    const dayInput = document.getElementById('id_day');
    const timeSelect = document.getElementById('id_time');

    dayInput.addEventListener('change', function () {
      const selectedDay = this.value;

      if (!selectedDay) return;

      fetch(`/appointments/available-times/?day=${selectedDay}`)
        .then(response => response.json())
        .then(data => {
          // Clear existing options
          timeSelect.innerHTML = '<option value="">Select a time</option>';

          if (data.available_times) {
            data.available_times.forEach(time => {
              const option = document.createElement('option');
              option.value = time;
              option.textContent = time;
              timeSelect.appendChild(option);
            });
          }
        });
    });
  });