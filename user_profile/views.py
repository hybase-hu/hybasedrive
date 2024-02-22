from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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


def login(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        next_url = request.GET['next']
        print(next_url)
        if user is not None:
            try:
                auth.login(request, user)
                messages.success(request, "Login successfully!")
                return redirect(next_url)
            except Exception as e:
                print(e)
                messages.error(request, "Login error: " + e)
        else:
            messages.warning(request, "Login data not valid!")

    return render(request, 'user_profile/login.html', {})
