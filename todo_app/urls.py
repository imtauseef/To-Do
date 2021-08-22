from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items', views.create_item, name='items'),
    path('deletion/<str:pk>/', views.delete_item, name='deletion'),
]
