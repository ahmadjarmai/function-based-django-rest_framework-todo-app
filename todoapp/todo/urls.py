from django.urls import path
from . import views

urlpatterns =[
    path('list/', views.List, name='list'),
    path('create/', views.Create, name='create'),
    path('update/<int:pk>/', views.Update, name='update'),
    path('detail/<int:pk>/', views.Detail, name='detail'),
    path('delete/<int:pk>/', views.Delete, name='delete'),

]
