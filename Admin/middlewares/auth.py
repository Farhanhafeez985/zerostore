from django.shortcuts import redirect


def adminPanel_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        returnUrl = request.META['PATH_INFO']
        if not request.session.get('username') == 'admin':
            return redirect(f'/admin?next={returnUrl}')
        response = get_response(request)
        return response

    return middleware
