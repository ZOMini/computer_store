from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import UpdateView

from magazine.forms import CategoryForm, ItemForm, NameForm, PhoneItemForm
from magazine.models import Category, Item, Name
from magazine.time_func import timeit


@timeit
def index(request):
    template = 'magazine/index.html'
    text = 'Это главная страница проекта My_project_6'
    last_items = Item.objects.filter(status='Order').order_by('-pub_date')[:10]
    context = {
        'last_items': last_items,
        'text': text,
        # 'page_obj': page_obj,
    }
    return render(request, template, context)

@timeit
def item_detail(request, item_id):
    template = 'magazine/one_item_full.html'
    text = '___carr_item____'
    curr_item = Item.objects.select_related('name',).get(id=item_id)
    context = {
        'curr_item': curr_item,
        'text': text,
        # 'page_obj': page_obj,
    }
    return render(request, template, context)

@timeit
@login_required()
@permission_required('magazine.change_item', raise_exception=True)
def item_edit(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    form = ItemForm(
        request.POST or None,
        files=request.FILES or None,
        instance=item
    )
    if form.is_valid():
        form.save()
        return redirect('magazine:item_detail', item_id=item_id)
    context = {
        'item': item,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'magazine/create_item.html', context) 

@timeit
@login_required()
@permission_required('magazine.add_item', raise_exception=True)
def item_create(request):
    template = 'magazine/create_item.html'
    form = ItemForm(request.POST, files=request.FILES or None)
    is_edit = False
    if form.is_valid():
        item = form.save(commit=False)
        item.author = request.user
        item.save()
        return redirect('magazine:item_detail', item.id)
    return render(request, template, {'form': form, is_edit: is_edit})

@timeit
def name_detail(request, name_id):
    template = 'magazine/one_name_full.html'
    text = '___Name_detail____'
    # name = Name.objects.prefetch_related('model_items').get(id=name_id)
    name = Name.objects.get(id=name_id)
    item_in_magaz = name.model_items.filter(status ='Magaz')
    item_in_store = name.model_items.filter(status ='Store')
    context = {
        'item_in_magaz': item_in_magaz,
        'item_in_store': item_in_store,
        'name': name,
        'text': text,
        # 'page_obj': page_obj,
    }
    return render(request, template, context)

@timeit
@login_required()
@permission_required('magazine.change_name', raise_exception=True)
def name_edit(request, name_id):
    name = get_object_or_404(Name, id=name_id)
    form = NameForm(
        request.POST or None,
        files=request.FILES or None,
        instance=name
    )
    if form.is_valid():
        form.save()
        return redirect('magazine:name_detail', name_id=name_id)
    context = {
        'name': name,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'magazine/create_name.html', context) 

@timeit
@login_required()
@permission_required('magazine.add_name', raise_exception=True)
def name_create(request):
    template = 'magazine/create_name.html'
    form = NameForm(request.POST, files=request.FILES or None)
    is_edit = False
    if form.is_valid():
        name = form.save(commit=False)
        name.author = request.user
        name.save()
        # return redirect('magazine:name_detail', name.id)
        return redirect('magazine:index')
    return render(request, template, {'form': form, is_edit: is_edit})

@timeit
def category_detail(request, category_id):
    template = 'magazine/one_category_full.html'
    text = '___carr_category____'
    category = Category.objects.get(id=category_id)
    category_names = category.category_name.all()[:10]
    context = {
        'names': category_names,
        'category': category,
        'text': text,
        # 'page_obj': page_obj,
    }
    return render(request, template, context)

@timeit
@login_required()
@permission_required('magazine.change_category', raise_exception=True)
def category_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    form = CategoryForm(
        request.POST or None,
        files=request.FILES or None,
        instance=category
    )
    if form.is_valid():
        form.save()
        return redirect('magazine:category_detail', category_id=category_id)
    context = {
        'category': category,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'magazine/create_category.html', context) 

@timeit
@login_required()
@permission_required('magazine.add_category', raise_exception=True)
def category_create(request):
    template = 'magazine/create_category.html'
    form = CategoryForm(request.POST, files=request.FILES or None)
    is_edit = False
    if form.is_valid():
        name = form.save(commit=False)
        name.author = request.user
        name.save()
        # return redirect('magazine:category_detail', name.id)
        return redirect('magazine:index')
    return render(request, template, {'form': form, is_edit: is_edit})


@timeit
def order(request, name_id):
    template = 'magazine/order.html'
    text = 'Заказ товара.'
    try:
        item = Item.objects.filter(status='Magaz', name=name_id)[0]
        item_id = item.id
    except:
        return render(request, 'magazine/result_text.html', {'text': 'Товара нет в наличии!'}) 
    form = PhoneItemForm(
        request.POST or None,
        files=request.FILES or None,
        instance=item
    )
    if form.is_valid():
        form.save()
        item.status = 'Order'
        item.save()
        return render(request, 'magazine/result_text.html', {'text': 'Товар заказан!'}) 
    context = {
        'item': item,
        'form': form,
        'name_id': name_id,
        'is_edit': True,
    }
    return render(request, template, context) 
