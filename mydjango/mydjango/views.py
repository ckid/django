from django.http.response import HttpResponse


def first_page(request):
    return HttpResponse('<p>Hello world</p>')
