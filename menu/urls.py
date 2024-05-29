from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('menu_item/',views.menu_item, name='menu_item'),
    path('menu_item/<int:menu_id>/',views.menu_details),
    path('menu/',views.index, name='menu'),
]
