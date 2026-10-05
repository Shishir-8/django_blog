from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from .forms import NewsletterForm
from blogs.models import NewsletterSubscriber

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True).order_by('-updated_at')
    posts = Blog.objects.filter(is_featured = False)
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts
    }

    return render(request, 'home.html', context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            
            # Simple staff check for redirect
            if user.is_staff or user.is_superuser:
                return redirect('dashboard')
            return redirect('home')  # Normal users go here
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})



def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register')
    else:
        form = RegistrationForm()

    context = {
        'form':form
    }

    return render(request, 'auth/register.html', context)



def logout_view(request):
    auth.logout(request)
    return redirect('home')

def newsletter_subscribe(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully subscribed!")
        else:
            messages.error(request, "Please enter a valid email address.")

    return redirect('home')