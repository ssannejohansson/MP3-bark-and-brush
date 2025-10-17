from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import SignUpForm, EmailLoginForm, UserUpdateForm


# Create your views here.
# User registration
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Account created successfully! You can now log in."
            )
            # Redirect to login page after signup
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"signup_form": form})


class EmailLoginView(LoginView):
    """
    Login view using email-based authentication
    """

    authentication_form = EmailLoginForm
    template_name = "registration/login.html"


@login_required
def my_account(request):
    """
    Display and update user account information
    """
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Your profile has been updated successfully!")
            return redirect("my_account")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "registration/account.html", {"user_form": form})
