# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| booking | [appointment_success.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/templates/booking/appointment_success.html) | Validated by direct input | ![screenshot](documentation/validation/html-booking-appointment_success.png) |  |
| booking | [book_appointment.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/templates/booking/book_appointment.html) | Validated by direct input | ![screenshot](documentation/validation/html-booking-book_appointment.png) | ⚠️ Notes: See below. |
| booking | [my_appointments.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/templates/booking/my_appointments.html) | Validated by direct input  | ![screenshot](documentation/validation/html-booking-my_appointments.png) |  |
| booking | [update_appointment.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/templates/booking/update_appointment.html) | Validated by direct input | ![screenshot](documentation/validation/html-booking-update_appointment.png) | ⚠️ Notes: See below. |
| registration | [account.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/registration/account.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Faccounts%2Faccount%2F) | ![screenshot](documentation/validation/html-booking-account.png) | ⚠️ Notes: See below. |
| registration | [login.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/registration/login.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/validation/html-booking-login.png) |  |
| registration | [signup.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/registration/signup.html) |[URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/validation/html-booking-signup.png) | ⚠️ Notes: See below. |
| registration| [password_reset_complete.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/registration/password_reset_complete.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Faccounts%2Freset%2Fdone%2F) | ![screenshot](documentation/validation/html-booking-password-reset-complete.png) |  |
| registration | [password_reset_confirm.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/registration/password_reset_confirm.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Faccounts%2Freset%2FMQ%2Fset-password%2F) | ![screenshot](documentation/validation/html-booking-password-reset-confirm.png) |  |
| registration | [password_reset_done.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/registration/password_reset_done.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Faccounts%2Fpassword_reset%2Fdone%2F) | ![screenshot](documentation/validation/html-booking-password-reset-done.png) | |
| registration | [password_reset_form.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/registration/password_reset_form.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Faccounts%2Fpassword_reset%2F) | ![screenshot](documentation/validation/html-booking-password-reset-form.png) | ⚠️ Notes: See below. |
| my_project | [404.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/404.html) | Validated by direct input | ![screenshot](documentation/validation/html-my_project-404.png) | ⚠️ Notes: See below. |
| my_project | [about.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/about.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Fabout%2F)| ![screenshot](documentation/validation/html-my_project-about.png) | ⚠️ Notes: see below. |
| my_project | [gallery.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/gallery.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Fgallery%2F)| ![screenshot](documentation/validation/html-my_project-gallery.png) | ⚠️ Notes: see below. |
| my_project | [index.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/index.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2F) | ![screenshot](documentation/validation/html-my_project-index.png) | ⚠️ Notes: see below.  |
| my_project | [services.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/services.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Fservices%2F) | ![screenshot](documentation/validation/html-my_project-services.png) | ⚠️ Notes: see below. |

⚠️ Note about Errors with the contact form:

Since the official Django documentation says to wrap forms inside of HTML form tags, I will keep this as it is.
![screenshot](documentation/django-doc-forms.png)

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| my_project | [styles.css](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/static/css/styles.css) | [URL](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv)| ![screenshot](documentation/validation/css-my_project-styles.png) |  |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| my_project | [script.js](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/static/js/script.js) |  | ![screenshot](documentation/validation/js-my_project-script.png) | |


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| accounts | [admin.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/accounts/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/accounts/admin.py) | | ⚠️ Notes: Empty file  |
| accounts | [models.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/accounts/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/accounts/models.py) | | ⚠️ Notes: Empty file |
| accounts | [tests.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/accounts/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/accounts/tests.py) |  | ⚠️ Notes: Empty file |
| accounts | [urls.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/accounts/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/accounts/urls.py) | ![screenshot](documentation/validation/py-accounts-urls.png) | |
| accounts | [views.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/accounts/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/accounts/views.py) | ![screenshot](documentation/validation/py-accounts-views.png) |  |
| booking | [admin.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/booking/admin.py) | ![screenshot](documentation/validation/py-booking-admin.png) | |
| booking | [forms.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/booking/forms.py) | ![screenshot](documentation/validation/py-booking-forms.png) |  |
| booking | [models.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/booking/models.py) | ![screenshot](documentation/validation/py-booking-models.png) | |
| booking | [tests.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/booking/tests.py) | | ⚠️ Notes: Empty file |
| booking | [urls.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/booking/urls.py) | ![screenshot](documentation/validation/py-booking-urls.png) | |
| booking | [views.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/booking/views.py) | ![screenshot](documentation/validation/py-booking-views.png) |  |
| main | [admin.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/main/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/main/admin.py) || ⚠️ Notes: Empty file |
| main | [models.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/main/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/main/models.py) |  | ⚠️ Notes: Empty file |
| main | [tests.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/main/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/main/tests.py) |  | ⚠️ Notes: Empty file |
| main | [urls.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/main/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/main/urls.py) | ![screenshot](documentation/validation/py-main-urls.png) | |
| main | [views.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/main/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/main/views.py) | ![screenshot](documentation/validation/py-main-views.png) | |
|  | [manage.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) |  |
| my_project | [settings.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/my_project/settings.py) | ![screenshot](documentation/validation/py-my_project-settings.png) | |
| my_project | [urls.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/my_project/urls.py) | ![screenshot](documentation/validation/py-my_project-urls.png) | |
| my_project | [urls.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/my_project/urls.py) | ![screenshot](documentation/validation/py-my_project-urls.png) | ⚠️ Notes (if applicable) |
| my_project | [views.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/my_project/views.py) | ![screenshot](documentation/validation/py-my_project-views.png) | ⚠️ Notes (if applicable) |


## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| About | ![screenshot](documentation/responsiveness/mobile-about.png) | ![screenshot](documentation/responsiveness/tablet-about.png) | ![screenshot](documentation/responsiveness/desktop-about.png) | Works as expected |
| Services | ![screenshot](documentation/responsiveness/mobile-services.png) | ![screenshot](documentation/responsiveness/tablet-services.png) | ![screenshot](documentation/responsiveness/desktop-services.png) | Works as expected |
| Gallery | ![screenshot](documentation/responsiveness/mobile-gallery.png) | ![screenshot](documentation/responsiveness/tablet-gallery.png) | ![screenshot](documentation/responsiveness/desktop-gallery.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |
| Contact Modal | ![screenshot](documentation/responsiveness/mobile-contact-modal.png) | ![screenshot](documentation/responsiveness/tablet-contact-modal.png) | ![screenshot](documentation/responsiveness/desktop-contact-modal.png) | Works as expected |
| Sign Up | ![screenshot](documentation/responsiveness/mobile-sign-up.png) | ![screenshot](documentation/responsiveness/tablet-sign-up.png) | ![screenshot](documentation/responsiveness/desktop-sign-up.png) | Works as expected |
| Log in | ![screenshot](documentation/responsiveness/mobile-log-in.png) | ![screenshot](documentation/responsiveness/tablet-log-in.png) | ![screenshot](documentation/responsiveness/desktop-log-in.png) | Works as expected |account
| Account | ![screenshot](documentation/responsiveness/mobile-account.png) | ![screenshot](documentation/responsiveness/tablet-account.png) | ![screenshot](documentation/responsiveness/desktop-account.png) | Works as expected |
| Book Appointment | ![screenshot](documentation/responsiveness/mobile-book-appointment.png) | ![screenshot](documentation/responsiveness/tablet-book-appointment.png) | ![screenshot](documentation/responsiveness/desktop-book-appointment.png) | Works as expected |
| Appointment Success | ![screenshot](documentation/responsiveness/mobile-appointment-success.png) | ![screenshot](documentation/responsiveness/tablet-appointment-success.png) | ![screenshot](documentation/responsiveness/desktop-appointment-success.png) | Works as expected |
| My Appointments | ![screenshot](documentation/responsiveness/mobile-my-appointments.png) | ![screenshot](documentation/responsiveness/tablet-my-appointments.png) | ![screenshot](documentation/responsiveness/desktop-my-appointments.png) | Works as expected |
| Update Appointment | ![screenshot](documentation/responsiveness/mobile-update-appointment.png) | ![screenshot](documentation/responsiveness/tablet-update-appointment.png) | ![screenshot](documentation/responsiveness/desktop-update-appointment.png) | Works as expected |
| Password Reset | ![screenshot](documentation/responsiveness/mobile-password-reset.png) | ![screenshot](documentation/responsiveness/tablet-password-reset.png) | ![screenshot](documentation/responsiveness/desktop-password-reset.png) | Works as expected |
| Password Reset Complete| ![screenshot](documentation/responsiveness/mobile-passsword-reset-complete.png) | ![screenshot](documentation/responsiveness/tablet-passsword-reset-complete.png) | ![screenshot](documentation/responsiveness/desktop-passsword-reset-complete.png) | Works as expected |
| Password Reset Done | ![screenshot](documentation/responsiveness/mobile-password-reset-done.png) | ![screenshot](documentation/responsiveness/tablet-password-reset-done.png) | ![screenshot](documentation/responsiveness/desktop-password-reset-done.png) | Works as expected |
| Password Reset Form | ![screenshot](documentation/responsiveness/mobile-password-reset-form.png) | ![screenshot](documentation/responsiveness/tablet-password-reset-form.png) | ![screenshot](documentation/responsiveness/desktop-password-reset-form.png) | Works as expected |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/safari-home.png) | Works as expected |
| About | ![screenshot](documentation/browsers/chrome-about.png) | ![screenshot](documentation/browsers/firefox-about.png) | ![screenshot](documentation/browsers/safari-about.png) | Works as expected |
| Services | ![screenshot](documentation/browsers/chrome-services.png) | ![screenshot](documentation/browsers/firefox-services.png) | ![screenshot](documentation/browsers/safari-services.png) | Works as expected |
| Gallery | ![screenshot](documentation/browsers/chrome-gallery.png) | ![screenshot](documentation/browsers/firefox-gallery.png) | ![screenshot](documentation/browsers/safari-gallery.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/safari-404.png) | Works as expected |
| Contact Modal | ![screenshot](documentation/browsers/chrome-contact-modal.png) | ![screenshot](documentation/browsers/firefox-contact-modal.png) | ![screenshot](documentation/browsers/safari-contact-modal.png) | Works as expected |
| Sign Up | ![screenshot](documentation/browsers/chrome-sign-up.png) | ![screenshot](documentation/browsers/firefox-sign-up.png) | ![screenshot](documentation/browsers/safari-sign-up.png) | Works as expected |
| Log In | ![screenshot](documentation/browsers/chrome-log-in.png) | ![screenshot](documentation/browsers/firefox-log-in.png) | ![screenshot](documentation/browsers/safari-log-in.png) | Works as expected |
| Account | ![screenshot](documentation/browsers/chrome-account.png) | ![screenshot](documentation/browsers/firefox-account.png) | ![screenshot](documentation/browsers/safari-account.png) | Works as expected |
| Book Appointment | ![screenshot](documentation/browsers/chrome-book-appointment.png) | ![screenshot](documentation/browsers/firefox-book-appointment.png) | ![screenshot](documentation/browsers/safari-book-appointment.png) | Works as expected |
| Appointment Success | ![screenshot](documentation/browsers/chrome-appointment-success.png) | ![screenshot](documentation/browsers/firefox-appointment-success.png) | ![screenshot](documentation/browsers/safari-appointment-success.png) | Works as expected |
| My Appointments | ![screenshot](documentation/browsers/chrome-my-appointments.png) | ![screenshot](documentation/browsers/firefox-my-appointments.png) | ![screenshot](documentation/browsers/safari-my-appointments.png) | Works as expected |
| Update Appointment | ![screenshot](documentation/browsers/chrome-update-appointment.png) | ![screenshot](documentation/browsers/firefox-update-appointment.png) | ![screenshot](documentation/browsers/safari-update-appointment.png) | Works as expected |
| Password Reset Complete | ![screenshot](documentation/browsers/chrome-password-reset-complete.png) | ![screenshot](documentation/browsers/firefox-password-reset-complete.png) | ![screenshot](documentation/browsers/safari-password-reset-complete.png) | Works as expected |
| Password Reset Form | ![screenshot](documentation/browsers/chrome-password-reset-form.png) | ![screenshot](documentation/browsers/firefox-password-reset-form.png) | ![screenshot](documentation/browsers/safari-password-reset-form.png) | Works as expected |
| Password Reset Done | ![screenshot](documentation/browsers/chrome-password-reset-done.png) | ![screenshot](documentation/browsers/firefox-password-reset-done.png) | ![screenshot](documentation/browsers/safari-password-reset-done.png) | Works as expected |
| Password Reset| ![screenshot](documentation/browsers/chrome-password-reset.png) | ![screenshot](documentation/browsers/firefox-password-reset.png) | ![screenshot](documentation/browsers/safari-password-reset.png) | Works as expected |

## Lighthouse Audit

⚠️ INSTRUCTIONS ⚠️

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| About | ![screenshot](documentation/lighthouse/mobile-about.png) | ![screenshot](documentation/lighthouse/desktop-about.png) |
| Services | ![screenshot](documentation/lighthouse/mobile-services.png) | ![screenshot](documentation/lighthouse/desktop-services.png) |
| Gallery | ![screenshot](documentation/lighthouse/mobile-gallery.png) | ![screenshot](documentation/lighthouse/desktop-gallery.png) |
| Sign Up | ![screenshot](documentation/lighthouse/mobile-sign-up.png) | ![screenshot](documentation/lighthouse/desktop-sign-up.png) |
| Log In | ![screenshot](documentation/lighthouse/mobile-log-in.png) | ![screenshot](documentation/lighthouse/desktop-log-in.png) |
| Account | ![screenshot](documentation/lighthouse/mobile-account.png) | ![screenshot](documentation/lighthouse/desktop-account.png) |
| Book Appointment | ![screenshot](documentation/lighthouse/mobile-book-appointment.png) | ![screenshot](documentation/lighthouse/desktop-book-appointment.png) |
| Appointment Success | ![screenshot](documentation/lighthouse/mobile-appointment-success.png) | ![screenshot](documentation/lighthouse/desktop-appointment-success.png) |
| My Appointments | ![screenshot](documentation/lighthouse/mobile-my-appointments.png) | ![screenshot](documentation/lighthouse/desktop-my-appointments.png) |
| Update Appointment | ![screenshot](documentation/lighthouse/mobile-update-appointment.png) | ![screenshot](documentation/lighthouse/desktop-update-appointment.png) |
| Password Reset Complete | ![screenshot](documentation/lighthouse/mobile-password-reset-complete.png) | ![screenshot](documentation/lighthouse/desktop-password-reset-complete.png) |
| Password Reset Confirm | ![screenshot](documentation/lighthouse/mobile-password-reset-confirm.png) | ![screenshot](documentation/lighthouse/desktop-password-reset-confirm.png) |
| Password Reset Done | ![screenshot](documentation/lighthouse/mobile-password-reset-done.png) | ![screenshot](documentation/lighthouse/desktop-password-reset-done.png) |
| Password Reset Form | ![screenshot](documentation/lighthouse/mobile-password-reset-form.png) | ![screenshot](documentation/lighthouse/desktop-password-reset-form.png) |

⚠️ NOTES: 
The lower performance scores on certain pages are primarily attributed to image sizes, despite having already been compressed. Compressing them further with free compressors is making them loose quality and look bad. Given the website’s relatively small scale, I therefore chose to leave them as they are for now. However, I recognize that in a real-world or larger-scale project with more images, further optimization and compression would be necessary to enhance performance.py

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Business Owner Management | Feature is expected to allow the business owner to create new bookings | Created a new booking | Booking was created successfully and displayed correctly in the booking system. | ![screenshot](documentation/defensive/create-booking.png) |
| | Feature is expected to allow the business owner to update existing booking | Edited the content of an existing booking | Booking was updated successfully with the new content. | ![screenshot](documentation/defensive/update-booking.png) |
| | Feature is expected to allow the business owner to delete bookings| Attempted to delete a booking, confirming the action before proceeding | Booking was deleted successfully. | ![screenshot](documentation/defensive/delete-booking.png) |
| | Feature is expected to retrieve a list of all booked appointments | Accessed the business owner dashboard to view all booked appointments | All booked appointments were displayed in a list view. | ![screenshot](documentation/defensive/booked-appointments.png) |
| User Authentication | Feature is expected to allow registered users to log in to the site. | Attempted to log in with valid and invalid credentials. | Login was successful with valid credentials; invalid credentials were rejected. | ![screenshot](documentation/defensive/login.png) |
| | Feature is expected to allow users to register for an account. | Registered a new user with unique credentials. | User account was created successfully. | ![screenshot](documentation/defensive/register-invalid.png)![screenshot](documentation/defensive/register-valid.png) |
| | Feature is expected to allow users to log out securely. | Logged out and tried accessing a restricted page. | Access was denied after logout, as expected. | ![screenshot](documentation/defensive/logout.png)![screenshot](documentation/defensive/logged-out-user.png) |
| User Booking | Feature is expected to allow registered users to book an appointment | Logged in and booked an appointment | Occupied time slots was grayed out and disabled | ![screenshot](documentation/defensive/disabled-times.png) |
| Prevent Double Booking | Feature is expected to disable already booked time slots to prevent double booking | Logged in and booked an appointment |  | ![screenshot](documentation/defensive/booking.png) |
| | Feature is expected to allow registered users to manage their appointments | Updated a booked appointment, canceled a booked appointment | Booked appointment got updated/canceled and notification was displayed as expected. | ![screenshot](documentation/defensive/update.png) [screenshot](documentation/defensive/cancel.png)|
| | Feature is expected to allow users to edit their account information | Edited account information | Changes was applied | ![screenshot](documentation/defensive/user-info.png) |
| Other Features | Guest and registered users are able to fill in a contact form to contact the business | Filled in the contact form and clicked "Send Message" | Both guest users and registered users are able to send a message | ![screenshot](documentation/defensive/message.png)![screenshot](documentation/defensive/message-success.png) ![screenshot](documentation/defensive/message-recieved.png)  ||

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a business owner|  I would like a responsive site with clear navigation that clearly communicates our services | so that our customers will stay on our site | ![screenshot](documentation/features/home.png) |
| As a business owner | I would like to have an admin site | so that I can manage bookings and users | ![screenshot](documentation/features/admin.png) |
| As a first time visitor | I would like to find a groomer | so that I can groom my dog |![screenshot](documentation/features/home.png) |
| As first time visitor | I would like to know more about the groomers | so that I know if they will go along with my dog | ![screenshot](documentation/features/about.png) |
| As a first time visitor | I would like to know what services the groomers provide | so that I know if they will meet my requirements | ![screenshot](documentation/features/services.png) |
| As a first time visitor | I would like to look at images of previous customers | so that I can decide if I like their services | ![screenshot](documentation/features/gallery.png) |
| As a first time visitor | I would like to book an appointment | so that I can get my dog groomed | ![screenshot](documentation/features/booking.png) |
| As a first time visitor | I would like to know the opening times | so that I can know if they suit me |![screenshot](documentation/features/opening-times.png) |
| As a returning customer | I would like to book an appointment | so that I can get my dog groomed |![screenshot](documentation/features/booking.png) |
| As a returning customer | I would like to get in touch with the groomers | so that I can ask potential questions | ![screenshot](documentation/features/contact.png) |
| As a returning customer | I would like to sign up for a newsletter | so that I can get all the news from the business | ![screenshot](documentation/features/newsletter.png) |
| As a frequent customer | I would like to book an appointment | so that I can get my dog groomed | ![screenshot](documentation/features/booking.png) |


## Additional testing

In addition to conducting my own testing, I shared the website with friends and family to ensure compatibility across various devices and operating systems. I also requested their feedback on the overall user flow to confirm that the site is intuitive, easy to understand, feels authentic and are simple to navigate for all users.

## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/ssannejohansson/MP3-bark-and-brush?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/ssannejohansson/MP3-bark-and-brush/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/ssannejohansson/MP3-bark-and-brush/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/ssannejohansson/MP3-bark-and-brush/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs.png)

### Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/ssannejohansson/MP3-bark-and-brush?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/ssannejohansson/MP3-bark-and-brush/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable. | ![screenshot](documentation/validation/html-booking-password-reset-complete.png) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

