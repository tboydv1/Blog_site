from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(pu)
    return render(request, 'blogsite/index.html', {})

def post_details(request):
    return render(request, 'blogsite/details.html', {})