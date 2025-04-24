from django.shortcuts import redirect

class FilterUnauthUsers:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if not request.user.is_authenticated and not request.path.startswith('/login'):
            from django.shortcuts import redirect
            return redirect('login')


        response = self.get_response(request)


        return response

        allowed_paths = ['/login/', '/signup/', '/admin/', '/admin/login/']
        if not request.user.is_authenticated and request.path not in allowed_paths:
            return redirect('login')
        return None
