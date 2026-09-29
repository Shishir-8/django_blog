from django.shortcuts import render
from blogs.models import Blog, Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required(login_url="/login")
def dashboard(request):
    categories_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    published_blogs = Blog.objects.filter(status="published").count()
    user_count = User.objects.all().count()

    recent_blogs = Blog.objects.select_related('category').order_by('-created_at')[:5]


    context = {
        'categories_count': categories_count,
        'blogs_count': blogs_count,
        'user_count': user_count,
        'published_blogs': published_blogs,
        'recent_blogs': recent_blogs
    }

    return render(request, 'dashboard/dashboard.html', context)


def categories(request):
    return render(request, 'dashboard/categories.html')



def blogs(request):
    return render(request, 'dashboard/blogs.html')