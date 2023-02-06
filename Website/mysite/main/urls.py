from django.urls import path
from . import views

# Create your url patterns here.

urlpatterns = [
    path('<int:id>', views.index, name = 'index'),
    path('', views.home, name = 'home'),
    path('create/', views.create, name = 'create'),
]