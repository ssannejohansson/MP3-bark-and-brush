# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

⚠️ INSTRUCTIONS ⚠️

1. [*recommended*] If you are using the live deployed site URLs, validate using this link: https://validator.w3.org/#validate_by_uri
2. Otherwise, if you are copying/pasting your HTML code manually, use this link: https://validator.w3.org/#validate_by_input

It's recommended to validate the live pages (all of them) using the deployed URL. This will give you a custom URL as well, which you can use below on your testing documentation. It makes it easier to return back to a page for validating it again in the future. The URL will look something like this:

- https://validator.w3.org/nu/?doc=https://ssannejohansson.github.io/MP3-bark-and-brush/index.html

⚠️ --- END --- ⚠️

🛑 IMPORTANT 🛑

RE: Python/Jinja syntax in HTML

Python projects that use Jinja syntax will not validate properly if you're copying/pasting into the HTML validator.

In order to properly validate these types of files, it's recommended to [validate by uri](https://validator.w3.org/#validate_by_uri) from the deployed Heroku pages.

Unfortunately, pages that require a user to be "logged-in" and authenticated (CRUD functionality) will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have access to login to an account on your project. In order to properly validate HTML pages with Jinja syntax for authenticated pages, follow these steps:

- Navigate to the deployed pages which require authentication.
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire "compiled" code, without any Jinja syntax.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated (e.g.: CRUD functionality).

🛑 ---- END --- 🛑

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
| registration| [password_reset_complete.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/registration/password_reset_complete.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Faccounts%2Freset%2Fdone%2F) | ![screenshot](documentation/validation/html-booking-password-reset-complete.png) | ⚠️ Notes (if applicable) |
| registration | [password_reset_confirm.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/registration/password_reset_confirm.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Faccounts%2Freset%2FMQ%2Fset-password%2F) | ![screenshot](documentation/validation/html-booking-password-reset-confirm.png) | ⚠️ Notes (if applicable) |
| registration | [password_reset_done.html](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/templates/registration/password_reset_done.html) | [URL](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbark-and-brush-dba8d291cd80.herokuapp.com%2Faccounts%2Fpassword_reset%2Fdone%2F) | ![screenshot](documentation/validation/html-booking-password-reset-done.png) | ⚠️ Notes (if applicable) |
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

⚠️ INSTRUCTIONS ⚠️

The [CI Python Linter](https://pep8ci.herokuapp.com) can be used two different ways.

- Copy/Paste your Python code directly into the linter.
- As an API, using the "raw" URL appended to the linter URL.
    - To find the "raw" URL, navigate to your file directly on the GitHub repo.
    - On that page, GitHub provides a button on the right called "Raw" that you can click.
    - From that new page, copy the full URL, and paste it after the CI Python Linter URL (with a `/` separator).

It's recommended to validate each file using the API URL. This will give you a custom URL which you can use on your testing documentation. It makes it easier to return back to a file for validating it again in the future. Use the steps above to generate your own custom URLs for each Python file.

**IMPORTANT**: `E501 line too long` errors

You must strive to fix all Python lines that are too long (>80 characters). In rare cases where you cannot break the lines [*without breaking the functionality*], adding "`  # noqa`" (*NO Quality Assurance*) to the end of those lines will ignore linting validation. Do not use "`  # noqa`" all over your project just to clear down validation errors! This can still cause a project to fail, for failing to fix actual PEP8 validation errors.

Sometimes variables can get too long, or excessive `if/else` conditional statements. These are acceptable instances to use the "`  # noqa`" comment.

When trying to fix "line too long" errors, try to avoid using `/` to split lines. A better approach would be to use any type of opening bracket, and hit `<Enter>` just after that. Any opening bracket type will work: `(`, `[`, `{`. By using an opening bracket, Python knows where to appropriately indent the next line of code, without having to *guess* for yourself and attempt to "tab" to the correct indentation level.

⚠️ --- END --- ⚠️

🛑 IMPORTANT 🛑

**IMPORTANT**: Django settings

The Django `settings.py` file comes with 4 lines that are quite long, and will throw the `E501 line too long` error. This is default behavior, but can be fixed by adding the "`  # noqa`" comment at the end of those lines.

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]
```

**IMPORTANT**: *migration* and *pycache* files

You do not have to validate files from the `migrations/` or `pycache/` folders! Ignore these `.py` files, and validate just the files that you've created or modified.

🛑 --- END --- 🛑

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| accounts | [admin.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/accounts/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/accounts/admin.py) | | ⚠️ Notes: Empty file  |
| accounts | [models.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/accounts/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/accounts/models.py) | | ⚠️ Notes: Empty file |
| accounts | [tests.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/accounts/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/accounts/tests.py) | ![screenshot](documentation/validation/py-accounts-tests.png) | ⚠️ Notes (if applicable) |
| accounts | [urls.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/accounts/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/accounts/urls.py) | ![screenshot](documentation/validation/py-accounts-urls.png) | |
| accounts | [views.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/accounts/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/accounts/views.py) | ![screenshot](documentation/validation/py-accounts-views.png) |  |
| booking | [admin.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/booking/admin.py) | ![screenshot](documentation/validation/py-booking-admin.png) | |
| booking | [forms.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/booking/forms.py) | ![screenshot](documentation/validation/py-booking-forms.png) |  |
| booking | [models.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/booking/models.py) | ![screenshot](documentation/validation/py-booking-models.png) | |
| booking | [tests.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/booking/tests.py) | ![screenshot](documentation/validation/py-booking-tests.png) | ⚠️ Notes (if applicable) |
| booking | [urls.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/booking/urls.py) | ![screenshot](documentation/validation/py-booking-urls.png) | |
| booking | [views.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/booking/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/booking/views.py) | ![screenshot](documentation/validation/py-booking-views.png) |  |
| main | [admin.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/main/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/main/admin.py) || ⚠️ Notes: Empty file |
| main | [models.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/main/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/main/models.py) |  | ⚠️ Notes: Empty file |
| main | [tests.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/main/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/main/tests.py) | ![screenshot](documentation/validation/py-main-tests.png) | ⚠️ Notes (if applicable) |
| main | [urls.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/main/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/main/urls.py) | ![screenshot](documentation/validation/py-main-urls.png) | |
| main | [views.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/main/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/main/views.py) | ![screenshot](documentation/validation/py-main-views.png) | |
|  | [manage.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) |  |
| my_project | [settings.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/my_project/settings.py) | ![screenshot](documentation/validation/py-my_project-settings.png) | |
| my_project | [urls.py](https://github.com/ssannejohansson/MP3-bark-and-brush/blob/main/my_project/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ssannejohansson/MP3-bark-and-brush/main/my_project/urls.py) | ![screenshot](documentation/validation/py-my_project-urls.png) | |


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

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports. Avoid testing the local version (Gitpod/VSCode/etc.), as this can have knock-on effects for performance. If you don't have "Lighthouse" in your Developer Tools, it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Unless your project is a single-page application (SPA), you should test Lighthouse Audit results for all of your pages, for both *mobile* and *desktop*.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

⚠️ --- END --- ⚠️

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| About | ![screenshot](documentation/lighthouse/mobile-about.png) | ![screenshot](documentation/lighthouse/desktop-about.png) |
| Services | ![screenshot](documentation/lighthouse/mobile-services.png) | ![screenshot](documentation/lighthouse/desktop-services.png) |
| Gallery | ![screenshot](documentation/lighthouse/mobile-gallery.png) | ![screenshot](documentation/lighthouse/desktop-gallery.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |
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

## Defensive Programming

⚠️ INSTRUCTIONS ⚠️

Defensive programming (defensive design) is extremely important! When building projects that accept user inputs or forms, you should always test the level of security for each form field. Examples of this could include (but not limited to):

All Projects:

- Users cannot submit an empty form (add the `required` attribute)
- Users must enter valid field types (ensure the correct input `type=""` is used)
- Users cannot brute-force a URL to navigate to a restricted pages

Python Projects:

- Users cannot perform CRUD functionality if not authenticated (if login functionality exists)
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers/admins

You'll want to test all functionality on your application, whether it's a standard form, or CRUD functionality, for data manipulation on a database. Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser). You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable (can someone else replicate the same outcome?). Ideally, tests cases should focus on each individual section of every page on the website. Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine, consider documenting tests on each element of the page (eg. button clicks, input box validation, navigation links, etc.) by testing them in their "happy flow", their "bad/exception flow", mentioning the expected and observed results, and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

- Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

⚠️ --- END --- ⚠️

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Blog Management | Feature is expected to allow the blog owner to create new posts with a title, featured image, and content. | Created a new post with valid title, image, and content data. | Post was created successfully and displayed correctly in the blog. | ![screenshot](documentation/defensive/create-post.png) |
| | Feature is expected to allow the blog owner to update existing posts. | Edited the content of an existing blog post. | Post was updated successfully with the new content. | ![screenshot](documentation/defensive/update-post.png) |
| | Feature is expected to allow the blog owner to delete blog posts. | Attempted to delete a blog post, confirming the action before proceeding. | Blog post was deleted successfully. | ![screenshot](documentation/defensive/delete-post.png) |
| | Feature is expected to retrieve a list of all published posts. | Accessed the blog owner dashboard to view all published posts. | All published posts were displayed in a list view. | ![screenshot](documentation/defensive/published-posts.png) |
| | Feature is expected to preview posts as drafts before publishing. | Created a draft post and previewed it. | Draft was displayed correctly in preview mode. | ![screenshot](documentation/defensive/preview-draft.png) |
| Comments Management | Feature is expected to allow the blog owner to approve or reject comments. | Approved and rejected comments from the dashboard. | Approved comments were published; rejected comments were removed. | ![screenshot](documentation/defensive/review-comments.png) |
| | Feature is expected to allow the blog owner to edit or delete comments. | Edited and deleted existing comments. | Comments were updated or removed successfully. | ![screenshot](documentation/defensive/edit-delete-comments.png) |
| User Authentication | Feature is expected to allow registered users to log in to the site. | Attempted to log in with valid and invalid credentials. | Login was successful with valid credentials; invalid credentials were rejected. | ![screenshot](documentation/defensive/login.png) |
| | Feature is expected to allow users to register for an account. | Registered a new user with unique credentials. | User account was created successfully. | ![screenshot](documentation/defensive/register.png) |
| | Feature is expected to allow users to log out securely. | Logged out and tried accessing a restricted page. | Access was denied after logout, as expected. | ![screenshot](documentation/defensive/logout.png) |
| User Comments | Feature is expected to allow registered users to leave comments on blog posts. | Logged in and added comments to a blog post. | Comments were successfully added and marked as pending approval. | ![screenshot](documentation/defensive/add-comment.png) |
| | Feature is expected to display a notification that comments are pending approval. | Added a comment and checked the notification message. | Notification was displayed as expected. | ![screenshot](documentation/defensive/pending-approval.png) |
| | Feature is expected to allow users to edit their own comments. | Edited personal comments. | Comments were updated as expected. | ![screenshot](documentation/defensive/edit-user-comments.png) |
| | Feature is expected to allow users to delete their own comments. | Deleted personal comments. | Comments were removed as expected. | ![screenshot](documentation/defensive/delete-user-comments.png) |
| Guest Features | Feature is expected to allow guest users to read blog posts without registering. | Opened blog posts as a guest user. | Blog posts were fully accessible without logging in. | ![screenshot](documentation/defensive/view-posts-guest.png) |
| | Feature is expected to display the names of other commenters on posts. | Checked the names of commenters on posts as a guest user. | Commenter names were displayed as expected. | ![screenshot](documentation/defensive/commenter-names.png) |
| | Feature is expected to block standard users from brute-forcing admin pages. | Attempted to navigate to admin-only pages by manipulating the URL (e.g., `/admin`). | Access was blocked, and a message was displayed showing denied access. | ![screenshot](documentation/defensive/brute-force.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

⚠️ INSTRUCTIONS ⚠️

Testing User Stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **Features** should already align with the **User Stories**, so this should be as simple as creating a table with the User Story, matching with the re-used screenshot from the respective Feature.

⚠️ --- END --- ⚠️

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a blog owner | I would like to create new blog posts with a title, featured image, and content | so that I can share my experiences with my audience. | ![screenshot](documentation/features/feature01.png) |
| As a blog owner | I would like to update existing blog posts | so that I can correct or add new information to my previous stories. | ![screenshot](documentation/features/feature02.png) |
| As a blog owner | I would like to delete blog posts | so that I can remove outdated or irrelevant content from my blog. | ![screenshot](documentation/features/feature03.png) |
| As a blog owner | I would like to retrieve a list of all my published blog posts | so that I can manage them from a central dashboard. | ![screenshot](documentation/features/feature04.png) |
| As a blog owner | I would like to preview a post as draft before publishing it | so that I can ensure formatting and content appear correctly. | ![screenshot](documentation/features/feature05.png) |
| As a blog owner | I would like to review comments before they are published | so that I can filter out spam or inappropriate content. | ![screenshot](documentation/features/feature06.png) |
| As a blog owner | I would like to approve or reject comments from users | so that I can maintain control over the discussion on my posts. | ![screenshot](documentation/features/feature07.png) |
| As a blog owner | I would like to view a list of all comments (both approved and pending) | so that I can manage user engagement effectively. | ![screenshot](documentation/features/feature08.png) |
| As a blog owner | I would like to edit or delete user comments | so that I can clean up or remove inappropriate responses after they've been posted. | ![screenshot](documentation/features/feature09.png) |
| As a registered user | I would like to log in to the site | so that I can leave comments on blog posts. | ![screenshot](documentation/features/feature10.png) |
| As a registered user | I would like to register for an account | so that I can become part of the community and engage with the blog. | ![screenshot](documentation/features/feature11.png) |
| As a registered user | I would like to leave a comment on a blog post | so that I can share my thoughts or ask questions about the owner's experiences. | ![screenshot](documentation/features/feature12.png) |
| As a registered user | I would like my comment to show my name and the timestamp | so that others can see who I am and when I left the comment. | ![screenshot](documentation/features/feature13.png) |
| As a registered user | I would like to receive a notification or message saying my comment is pending approval | so that I understand it hasn't been posted immediately. | ![screenshot](documentation/features/feature14.png) |
| As a registered user | I would like to edit or delete my own comments | so that I can fix mistakes or retract my statement. | ![screenshot](documentation/features/feature15.png) |
| As a guest user | I would like to read blog posts without registering | so that I can enjoy the content without needing to log in. | ![screenshot](documentation/features/feature16.png) |
| As a guest user | I would like to browse past posts | so that I can explore the blog's full content history. | ![screenshot](documentation/features/feature17.png) |
| As a guest user | I would like to register for an account | so that I can participate in the community by leaving comments on posts. | ![screenshot](documentation/features/feature18.png) |
| As a guest user | I would like to see the names of other commenters on posts | so that I can get a sense of community interaction before registering. | ![screenshot](documentation/features/feature19.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/feature20.png) |

## Additional testing

In addition to conducting my own testing, I shared the website with friends and family to ensure compatibility across various devices and operating systems. I also requested their feedback on the overall user flow to confirm that the site is intuitive, easy to understand, feels authentic and are simple to navigate for all users.

## Bugs

⚠️ INSTRUCTIONS ⚠️

Nobody likes bugs,... except the assessors! Projects seem more suspicious if a student doesn't properly track their bugs. If you're about to submit your project without any bugs listed below, you should ask yourself why you're doing this course in the first place, if you're able to build this entire application without running into any bugs. The best thing you can do for any project is to document your bugs! Not only does it show the true stages of development, but think of it as breadcrumbs for yourself in the future, should you encounter the same/similar bug again, it acts as a gentle reminder on what you did to fix the bug.

If/when you encounter bugs during the development stages of your project, you should document them here, ideally with a screenshot explaining what the issue was, and what you did to fix the bug.

Alternatively, an improved way to manage bugs is to use the built-in **[Issues](https://www.github.com/ssannejohansson/MP3-bark-and-brush/issues)** tracker on your GitHub repository. This can be found at the top of your repository, the tab called "Issues".

If using the Issues tracker for bug management, you can simplify the documentation process for testing. Issues allow you to directly paste screenshots into the issue page without having to first save the screenshot locally. You can add labels to your issues (e.g. `bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s). Once you've solved the issue/bug, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following examples below.

⚠️ --- END --- ⚠️

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/ssannejohansson/MP3-bark-and-brush?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/ssannejohansson/MP3-bark-and-brush/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/ssannejohansson/MP3-bark-and-brush/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/ssannejohansson/MP3-bark-and-brush/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

⚠️ INSTRUCTIONS ⚠️

You will need to mention any unfixed bugs and why they are not fixed upon submission of your project. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. Where possible, you must fix all outstanding bugs, unless outside of your control.

If you've identified any unfixed bugs, no matter how small, be sure to list them here! It's better to be honest and list them, because if it's not documented and an assessor finds the issue, they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

⚠️ --- END --- ⚠️

[![GitHub issue custom search](https://img.shields.io/github/issues-search/ssannejohansson/MP3-bark-and-brush?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/ssannejohansson/MP3-bark-and-brush/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/ssannejohansson/MP3-bark-and-brush/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. | ![screenshot](documentation/issues/poor-responsiveness.png) |
| When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable. | ![screenshot](documentation/issues/section-header.png) |
| Validation errors on "signup.html" coming from the Django Allauth package. | ![screenshot](documentation/issues/allauth.png) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

