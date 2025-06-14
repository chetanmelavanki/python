from django.shortcuts import render
from .models import Post, Category

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def category_posts(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = category.posts.all()
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
