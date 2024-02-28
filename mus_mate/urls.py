from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("forum.urls", namespace="forum")),
    path("__debug__/", include("debug_toolbar.urls")),
]
