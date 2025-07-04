from django.shortcuts import render

# Create your views here.
from .models import VlogPost

def home(request):
    posts = VlogPost.objects.order_by('-created_at')
    return render(request, 'vlog/home.html', {'posts': posts})
