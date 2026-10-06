from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect



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
    single_blog = get_object_or_404(Blog, slug=slug, status="published")
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(blog=single_blog)
    context = {
        'single_blog': single_blog,
        'comments': comments
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


