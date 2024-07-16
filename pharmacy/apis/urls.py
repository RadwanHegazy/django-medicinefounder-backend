from .views import get, create
from django.urls import path

urlpatterns = [
    path('get/', get.get_medicine.as_view(),name='get_list'),
    path('create/', create.create_medicine.as_view(),name='create_medicine'),
]