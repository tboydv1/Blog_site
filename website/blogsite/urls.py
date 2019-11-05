from django.urls import path
from . import views

urlpatterns = [

    path('', views.post_list, name = "index"),
    path('details/', views.post_details, name= "details")
]
