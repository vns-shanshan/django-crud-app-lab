from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dog_index, name='dog-index'),
    path('dogs/<int:dog_id>/', views.dog_detail, name='dog-detail')
]