from django.shortcuts import render

menu = [
    {'name': 'Home', 'url': 'main:home'},
    {'name': 'About', 'url': 'main:about'},
    {'name': 'Play', 'url': 'main:play'},
]


def index(request):
    context = {
        'title': 'Home',
        'menu': menu,
        'active_link': 'Home',
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'About',
        'menu': menu,
        'active_link': 'About',
    }
    return render(request, 'main/about.html', context=context)


def play(request):
    context = {
        'title': 'Play',
        'menu': menu,
        'active_link': 'Play',
    }
    return render(request, 'main/play.html', context=context)


# region Error Handlers
def bad_request(request, exception):
    context = {
        'title': '400',
        'error_code': '400',
        'header': 'Incorrect Request',
        'text': 'We are deeply sorry, but the server is unable to process your request correctly. ' +
                'Contact support for more information'
    }
    return render(request, 'main/server_errors.html', context=context)


def page_not_fount(request, exception):
    context = {
        'title': '404',
        'error_code': '404',
        'header': 'Page Not Found',
        'text': 'Unfortunately, we could not find the page you are looking for. ' +
                'Contact support for more information'
    }
    return render(request, 'main/server_errors.html', context=context)


def access_denied(request, exception):
    context = {
        'title': '403',
        'error_code': '403',
        'header': 'Access Denied',
        'text': 'We are deeply sorry, but you have no access to this page. ' +
                'Contact support for more information'
    }
    return render(request, 'main/server_errors.html', context=context)


def server_error(request):
    context = {
        'title': '500',
        'error_code': '500',
        'header': 'Server Error',
        'text': 'We are deeply sorry, but the server ran into some issues processing your request. ' +
                'Contact support for more information'
    }
    return render(request, 'main/server_errors.html', context=context)
# endregion
