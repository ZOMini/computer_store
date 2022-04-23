from django.shortcuts import render

from magazine.models import Item
from magazine.time_func import timeit


@timeit
def index(request):
    template = 'magazine/index.html'
    text = 'Это главная страница проекта My_project_6'
    last_items = Item.objects.order_by('-pub_date')[:10]
    context = {
        'last_items': last_items,
        'text': text,
        # 'page_obj': page_obj,
    }
    return render(request, template, context)
