from django.urls import path
from . import views

urlpatterns = [
    path('baraa/', views.baraa, name='baraa'),
]