from django.shortcuts import render
from . models import MenuItem
from django.http import HttpResponse

def index(request):
    menu = MenuItem.objects.all()
    sorted_menu_items = sorted(menu, key=lambda menuItem: menuItem.name)
    return render(request, 'index.html',{'menu': sorted_menu_items})

def menu_item(request):
    return render(request, 'menu_details.html')


def menu_details(request, menu_id):
    menu_item = MenuItem.objects.get(pk=menu_id)
    return render(
        request,
        'menu_details.html',
        {'menu_item': menu_item}
    )