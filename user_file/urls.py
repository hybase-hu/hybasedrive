"""
URL configuration for hybasedrive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from user_file.views import list_my_files, download_file, upload_files, delete_file, view_file, \
    list_shared_with_me_files
from user_profile.views import index

urlpatterns = [
    path('my_files/', list_my_files, name='my_files'),
    path('shared_with_me/', list_shared_with_me_files, name='list_shared_with_me_files'),
    path('upload',upload_files,name="upload_files"),
    path('download/<int:file_pk>', download_file, name="download_file"),
    path('delete/<int:file_pk>', delete_file, name="delete_file"),
    path('view_file/<int:file_pk>', view_file, name="view_file"),
]
