from django.shortcuts import HttpResponse


def some_view(request):
    print(request.session.items())
    return HttpResponse("Request is", request)
