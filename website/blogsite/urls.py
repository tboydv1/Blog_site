from django.urls import path
from . import views

urlpatterns = [

    path('', views.post_list, name = "index"),
    path('post/<int:pk>/', views.post_details, name= "details")
]
