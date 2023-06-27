from django.shortcuts import redirect


## login check decorator
## redirect to login page if user is not authenticated
## import this to other apps for login status check
## add '@login_required'
def login_required(func):
    def wrapper(request, *args, **kwargs):
        ## Login status check
        if not request.user.is_authenticated:
            return redirect('users:login')
        
        return func(request, *args, **kwargs)
    
    return wrapper