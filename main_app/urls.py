from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.ItemCreate.as_view(), name='items_create'),
    path('delete/<int:pk>/', views.ItemDelete.as_view(), name='items_delete'),
]