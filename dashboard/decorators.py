from functools import wraps
from django.shortcuts import redirect

def dashboard_required(view_func):

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        
        if not request.user.is_authenticated:
            return redirect('login') 

       
        if request.user.is_staff or request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        return redirect('home')  

    return _wrapped_view