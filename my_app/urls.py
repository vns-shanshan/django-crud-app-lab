from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dog_index, name='dog-index'),
    path('dogs/<int:dog_id>/', views.dog_detail, name='dog-detail'),
    path('dogs/create/', views.DogCreate.as_view(), name='dog-create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dog-update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dog-delete'),
    path('dogs/<int:dog_id>/add-feeding/', views.add_feeding, name='add-feeding'),
    path('toys/create/', views.ToyCreate.as_view(), name="toy-create"),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
    path('toys/', views.ToyList.as_view(), name='toy-index'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
    path('dogs/<int:dog_id>/associate-toy/<int:toy_id>/', views.associate_toy, name='associate-toy'),
    path('dogs/<int:dog_id>/remove-toy/<int:toy_id>/', views.remove_toy, name='remove-toy')
]