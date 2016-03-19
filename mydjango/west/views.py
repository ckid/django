from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import csrf

from west.models import Character


def first_page(request):
    return HttpResponse('<p>西餐</p>')


def staff (request):
    staff_list = Character.objects.all()
    staff_str = map(str, staff_list)

    return  HttpResponse("<p>" + ' '.join(staff_str) + "</p>")


def templay(request):
    context = {}
    context['label'] = 'Hello World'
    staff_list = Character.objects.all()
    staff_str = map(str, staff_list)
    context['staff'] = ' '.join(staff_str)
    context['staffs'] = staff_list;

    return render(request, 'templay.html', context)


def form(request):
    return render(request, 'form.html')


def investigate(request):
    csx = {}
    csx.update(csrf(request))
    if request.POST:
        submmit = request.POST['staff']
        if len(submmit):
            new_record = Character(name=submmit)
            new_record.save()
    all_records = Character.objects.all()
    csx['staff'] = all_records
    return render(request, "investigate.html", csx)