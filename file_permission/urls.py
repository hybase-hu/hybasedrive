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

from file_permission.views import add_permission, delete_permission
from user_file.views import list_my_files, download_file, upload_files, delete_file, view_file
from user_profile.views import index

app_name = "permission"

urlpatterns = [
    path('add_permission/', add_permission, name='add_permission'),
    path('delete_permission/<int:file_pk>/<int:user_pk>', delete_permission, name='delete_permission'),
]
