from django.shortcuts import render, get_object_or_404
from .models import Blog, Category



# Create your views here.

def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Blog.objects.filter(status='published', category=category)
    context = {
        'posts': posts,
        'category': category,

    }
    return render(request, 'post_by_category.html', context)


def blogs(request, slug):
    return render(request, 'blogs.html')