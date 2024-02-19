from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from file_permission.models import UploadFilePermission
from user_file.models import UploadFile


# Create your views here.
@login_required(login_url="login")
def add_permission(request):
    if request.method == 'POST':
        username = request.POST['username']
        file_pk = request.POST['file_pk']
        if username is not None and file_pk is not None:
            try:
                user = User.objects.get(username=username)
                file = UploadFile.objects.get(pk=file_pk)
                UploadFilePermission.objects.create(file=file, user=user)
                messages.success(request, "Add users [{0}] permission to file".format(user.username))
                return redirect('view_file', file_pk)
            except IntegrityError as e:
                messages.warning(request, "This file is already shared with this user [{}]".format(user))
                return redirect('view_file', file_pk)
            except Exception as e:
                messages.error(request, e)
                return redirect('view_file', file_pk)
        else:
            messages.warning(request, "Username is required")

    return redirect("my_files")


@login_required(login_url="login")
def delete_permission(request, file_pk, user_pk):
    user = request.user
    file = UploadFile.objects.get(pk=file_pk)
    if file.owner == user:
        UploadFilePermission.objects.get(file=file, user__pk=user_pk).delete()
        messages.success(request, "User shared permission is deleted")
        return redirect('view_file', file_pk)
    else:
        messages.error(request, "Permission Denied!")
    return redirect('view_file', file_pk)
