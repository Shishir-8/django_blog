
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blogs import views as BlogView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),

    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),

    path('', include('blogs.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
