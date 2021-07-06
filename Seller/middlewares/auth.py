from django.shortcuts import redirect


def sellerPanel_middleware(get_response,id=None):
    # One-time configuration and initialization.

    def middleware(request):
        returnUrl = request.META['PATH_INFO']
        if not request.session.get('type') == 'seller':
            return redirect(f'/login?next={returnUrl}')
        response = get_response(request)
        return response

    return middleware
