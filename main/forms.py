from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from crispy_forms.bootstrap import StrictButton


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control shadow-none",
            "placeholder": "Your name",
            "required": "required"
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control shadow-none",
            "placeholder": "Your email",
            "required": "required"
        })
    )
    phone = forms.CharField(
        label="Phone number",
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control shadow-none",
            "placeholder": "Your phone number",
            "required": "required"
        })
    )
    subject = forms.CharField(
        label="Subject",
        widget=forms.TextInput(attrs={
            "class": "form-control shadow-none",
            "placeholder": "Subject"}),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "class": "form-control shadow-none",
            "placeholder": "Your message",
            "rows": 6,
            "required": "required"
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Crispy Form helper setup
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'contact-form'

        # Crispy layout
        self.helper.layout = Layout(
            Row(Column('name', css_class='col-md-12')),
            Row(Column('email', css_class='col-md-12')),
            Row(Column('phone', css_class='col-md-12')),
            Row(Column('subject', css_class='col-md-12')),
            Row(Column('message', css_class='col-md-12')),
            StrictButton(
                'Send Message',
                type='submit',
                css_class='custom-btn-booking'
            )
        )