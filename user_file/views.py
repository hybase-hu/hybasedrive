from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect

from user_file.forms import UploadFileForms
from user_file.models import UploadFile
from user_profile.models import UserProfile


# Create your views here.
@login_required(login_url="login")
def list_my_files(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    # user_files = UploadFile.objects.filter(owner=user).all()
    user_files = user.my_files.all()

    context = {
        "my_files": user_files
    }

    return render(request, "user_file/my_files.html", context)


@login_required(login_url="login")
def list_shared_with_me_files(request):
    user = request.user
    shared_with_me_files = user.shared_with_me.all()
    context = {
        "shared_with_me_files": shared_with_me_files
    }

    return render(request, "user_file/shared_with_me_files.html", context)


@login_required(login_url="login")
def download_file(request, file_pk):
    obj = UploadFile.objects.get(pk=file_pk)
    response = FileResponse(open(obj.file.path, 'rb'))
    print(obj.file)
    response['Content-Disposition'] = f'attachment; filename="{obj.filename()}"'
    response['Content-Type'] = 'application/octet-stream'

    return response


@login_required(login_url="login")
def upload_files(request):
    form = UploadFileForms()
    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    if request.method == "POST":
        for file in request.FILES.getlist('upload_files'):

            if file.size < user_profile.is_space_available():
                UploadFile.objects.create(owner=user, file_type=1, file=file, description=request.POST['description'])
            else:
                messages.error(request, "Run out of storage space: " + str(file))
                return redirect('index')

        messages.success(request, "File uploaded successfully!")
        return redirect('my_files')

    context = {
        'form': form
    }
    return render(request, 'user_file/upload_files.html', context)


@login_required(login_url="login")
def delete_file(request, file_pk):
    user = request.user
    file = UploadFile.objects.get(pk=file_pk)
    if file.owner == user:
        file.delete()
        messages.success(request, "File delete successfully!")
    else:
        messages.error(request, "Not permitted delete this file!")
    return redirect('my_files')


@login_required(login_url="login")
def view_file(request, file_pk):
    user = request.user
    file = UploadFile.objects.get(pk=file_pk)
    users_permissions = file.all_permissions.all()
    context = {
        "file": file,
        "user_permissions": users_permissions
    }
    print(users_permissions)

    if file.owner == user:
        return render(request, "user_file/view_file.html", context)
    else:
        messages.error(request, "Not permitted delete this file!")
