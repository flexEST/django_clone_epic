from django.contrib import admin
from django.urls import path
from epic_games import views  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("epic_games/", views.home, name="home"),
]
