from django.urls import path
from django.contrib import admin
from my_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello)
]