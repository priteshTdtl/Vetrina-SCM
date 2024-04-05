from django.shortcuts import redirect

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path.startswith('/dashboard'):
            return redirect('/sign-in')  # Redirect to login page if not authenticated

        response = self.get_response(request)
        return response
