from django.contrib import admin
from django.urls import include, path

from users.urls import users_api_v1_urls

api_v1_urls = [
    path("users/", include(users_api_v1_urls)),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_v1_urls)),
]
