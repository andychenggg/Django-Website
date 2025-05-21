from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("view/", views.view, name="index"),
path("home/", views.home, name="home"),
path("create/", views.get_name, name="index"),
path("<int:id>", views.index, name="index"),
path('delete/<int:id>/', views.delete_list, name='delete_list'),

]
