from django.contrib import admin
from django.urls import include, path
# from . import views

urlpatterns = [
    path("login/", include("login.urls")),
    path("login/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
]