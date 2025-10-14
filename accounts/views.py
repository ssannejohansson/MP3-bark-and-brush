from django.shortcuts import render, redirect
from .forms import SignUpForm, EmailLoginForm
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
    return render(request, 'registration/signup.html', {'form': form})


class EmailLoginView(LoginView):
    authentication_form = EmailLoginForm
    template_name = 'registration/login.html'