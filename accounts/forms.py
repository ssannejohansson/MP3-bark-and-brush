from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from crispy_forms.bootstrap import StrictButton


class SignUpForm(forms.ModelForm):
    """
    Form for creating a new user account
    """

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]

    def __init__(self, *args, **kwargs):
        # Initializes the form and set up Crispy Forms Helper
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_id = "signup-form"

        # Crispy layout
        self.helper.layout = Layout(
            Row(
                Column("first_name", css_class="col-md-6"),
                Column("last_name", css_class="col-md-6"),
            ),
            Row(Column("email", css_class="col-md-12")),
            Row(Column("password", css_class="col-md-12")),
            StrictButton(
                "Sign Up", "Sign Up", type="submit", css_class="custom-btn-booking"
            ),
        )

    def clean_email(self):
        # Prevents duplicate email registration
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        # Creates a new user
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        # Base username from email prefix
        base_username = email.split("@")[0]
        username = base_username
        counter = 1

        # Ensures username is unique
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        user = User(
            username=username, email=email, first_name=first_name, last_name=last_name
        )
        user.set_password(password)
        if commit:
            user.save()
        return user


class EmailLoginForm(AuthenticationForm):
    """
    Login form that authenticates users using email instead of username
    """

    username = forms.EmailField(label="Email")

    def clean(self):
        # Validates email and password combination
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise forms.ValidationError("Invalid email or password")
        return super().clean()


class CustomPasswordResetForm(PasswordResetForm):
    """
    Password reset form
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_id = "password-reset-form"

        # Crispy layout
        self.helper.layout = Layout(
            Row(Column("email", css_class="col-md-12")),
            StrictButton(
                "Reset Password", type="submit", css_class="custom-btn-booking"
            ),
        )

        # Customize widget styling
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control shadow-none",
                "placeholder": "Enter your account email",
            }
        )
        self.fields["email"].label = ""


class UserUpdateForm(forms.ModelForm):
    """
    Form for updating user details
    """

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_id = "user-update-form"

        # Crispy layout
        self.helper.layout = Layout(
            Row(
                Column("first_name", css_class="col-md-6"),
                Column("last_name", css_class="col-md-6"),
            ),
            Row(
                Column("email", css_class="col-md-12"),
            ),
            StrictButton(
                "Save Changes" '<i class="fa-solid fa-floppy-disk ms-2"></i>',
                "Save Changes",
                type="submit",
                css_class="custom-btn-booking",
            ),
        )
