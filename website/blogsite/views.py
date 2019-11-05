from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blogsite/index.html', {'posts':posts})

def post_details(request):
    posts_details = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blogsite/details.html', {'posts':posts_details.content})