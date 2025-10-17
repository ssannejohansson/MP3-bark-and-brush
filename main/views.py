from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def gallery(request):
    return render(request, "gallery.html")


def booking(request):
    return render(request, "book-now.html")


def book_login(request):
    return render(request, "registration/login.html")


class SuccessView(TemplateView):
    """
    Redirects to base.html after successful form submission
    """

    template_name = "base.html"


class ContactView(FormView):
    """
    Displays and processes the contact form
    """

    form_class = ContactForm
    template_name = "base.html"

    def form_valid(self, form):
        """
        Triggered when form is valid and sends an email with submitted form
        data
        """
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        phone = form.cleaned_data.get("phone")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        # Email layout
        full_message = f"""
            From: {name}
            {email}
            {phone}
            ________________________
            {message}
            """
        send_mail(
            subject=f"{subject}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )

        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse(
                {
                    "success": True,
                    "message": "Your message has been sent successfully! 🐾",
                }
            )

        # Fallback (if user has JS disabled)
        messages.success(self.request,
                         "Your message has been sent successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        """
        Defines where to redirect after successful form submission
        """
        return reverse("home")
