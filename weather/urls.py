from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), #amlost same as the path in the main app
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
]
