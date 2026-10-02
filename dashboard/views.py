from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Blog, Category
from django.contrib.auth.models import User
from .decorators import dashboard_required
from .forms import CategoryForm, BlogForm
from django.template.defaultfilters import slugify # for automatic slug generate in dashboard 
# Create your views here.

@dashboard_required
def dashboard(request):

    if not (request.user.is_staff or request.user.is_superuser):
        return redirect('home')
    
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

@dashboard_required
def categories(request):
    return render(request, 'dashboard/categories.html')


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_category.html', context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit_category.html', context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')


@dashboard_required
def blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'dashboard/blogs.html',context)


def add_blogs(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)                # request.files is used for form with image
        if form.is_valid():
            blog = form.save(commit=False)                             # temporarily save the form
            blog.author = request.user                   # by doing this author is request.user who write blog saved automatically
            blog.save()                           # by saving we get blog.id
                                                        
            blog.slug = f"{slugify(blog.title)-{blog.id}}"         # this makes slug unique
            blog.save()                                                  # finaly blog is created
            return redirect('blogs')
        else:
            print(form.errors)

    form = BlogForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_blogs.html', context)


def edit_blogs(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)      # before saving anything commit False
            blog.slug = f"{slugify(blog.title)}-{blog.id}"
            blog.save()
            return redirect('blogs')
    else:
        form = BlogForm(instance=blog)
    context = {
        'form': form,
        'blog': blog
    }
    return render(request, 'dashboard/edit_blogs.html', context)


def delete_blogs(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('blogs')