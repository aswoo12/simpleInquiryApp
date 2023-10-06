from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages



def registration(request):
    if request.method == 'POST':
        # Create a form that has request.POST
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Set the user's password securely
            username = form.cleaned_data['username']         
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                user.set_password(password1)
                user.save()
                
                messages.success(request, f'Your Account has been created {username} ! Proceed to log in')
                return redirect('login')  # Redirect to the login page
            else:
                # Handle password mismatch error here
                form.add_error('password2', 'Passwords entered do not match')
    else:
        form = RegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

def base(request):
    return render(request, "users/base.html")

def home(request):
    return render(request, "users/home.html")


    