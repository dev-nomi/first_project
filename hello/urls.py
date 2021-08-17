from django.urls import path
from . import views

urlpatterns = [
  path('',views.index,name='index'),
  path('noman',views.noman,name='noman'),
  path('<str:name>',views.greet,name='greet')
]