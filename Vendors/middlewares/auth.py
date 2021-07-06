from django.shortcuts import redirect


def vendorPanel_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        returnUrl = request.META['PATH_INFO']
        if not request.session.get('type') == 'vendor':
            return redirect(f'/login?next={returnUrl}')
        response = get_response(request)
        return response

    return middleware
