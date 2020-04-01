from django.urls import path
from . import views

                
urlpatterns = [
    path('', views.index),
    path('add/', views.addBook),
    path('<int:id>/', views.bookPage),
    path('<int:id>/delete/', views.delete),
    path('<int:id>/addReview/', views.addReview)
]