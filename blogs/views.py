from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from django.db.models import Q



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
    single_blog = get_object_or_404(Blog, slug=slug, status="published").strip()
    context = {
        'single_blog': single_blog
    }
    return render(request, 'single_blog.html', context)



def search(request):
    keywords = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keywords) | Q(short_description__icontains=keywords) | Q(blog_body__icontains=keywords), status="published")

    context = {
        'blogs': blogs,
        'keywords': keywords
    }

    return render(request, 'search.html', context)