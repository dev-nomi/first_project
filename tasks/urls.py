from django.urls import path
from . import views


app_name = "tasks" #to uniquely each app views
urlpatterns = [
  path('',views.index,name="index"),
  path('new',views.new,name="new")
]