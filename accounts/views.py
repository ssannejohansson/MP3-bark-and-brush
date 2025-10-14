from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, EmailLoginForm, UserUpdateForm
from django.contrib.auth.views import LoginView



# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'signup_form': form})


class EmailLoginView(LoginView):
    authentication_form = EmailLoginForm
    template_name = 'registration/login.html'


@login_required
def my_account(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('my_account')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'registration/account.html', {'user_form': form})