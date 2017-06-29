from django.shortcuts import render


def house_list(request):
    return render(request, 'list.html')


def house_detail(request, house_id):
    return render(request, 'detail.html')
