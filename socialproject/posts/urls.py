from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('', views.index, name='posts_index')
]