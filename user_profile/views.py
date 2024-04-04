from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from user_profile.forms import UserForm
from user_profile.models import UserProfile


# Create your views here.
@login_required(login_url="login")
def index(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    context = {
        "user_profile": user_profile
    }
    return render(request, 'user_profile/user_profile.html', context)


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect("index")


def register(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            passw1 = form.cleaned_data['password']
            passw2 = form.cleaned_data['confirm_password']
            if passw1 != passw2:
                messages.error(request, "Passwords not equal")
                return redirect('register')
            user = form.save(commit=False)
            user.set_password(passw2)
            user.save()
        else:
            messages.error(request, form.errors)
            return redirect('register')

    context = {
        'form': form
    }
    return render(request, 'user_profile/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            try:
                auth.login(request, user)
                messages.success(request, "Login successfully!")
                if request.GET.get('next'):
                    next_url = request.GET.get('next')
                    return redirect(next_url)
                else:
                    return redirect('index')
            except Exception as e:
                print(e)
                messages.error(request, "Login error: " + e)
        else:
            messages.warning(request, "Login data not valid!")

    return render(request, 'user_profile/login.html', {})
