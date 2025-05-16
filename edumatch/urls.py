from django.contrib import admin
from django.urls import include, path  # Добавьте include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cards.urls")),  # Эта строка подключает ваши страницы
]
