from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Item, Category
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
# Create your views here.


def search(request):

    items = Item.objects.filter(is_sold=False)

    category_id = request.GET.get('category', 0)
    if category_id:
        items = items.filter(category_id=category_id)

    searched_item = request.GET.get('search', '')
    if searched_item:
        items = Item.objects.filter(Q(name__icontains=searched_item) | Q(description__icontains=searched_item))

    categories = Category.objects.all()

    return render(request, 'item/items.html',{
        'items': items,
        'searched_item': searched_item,
        'categories': categories,
        'category_id': int(category_id),
    })


def detail(request, item_id):

    item = get_object_or_404(Item, pk=item_id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item_id)[:]

    return render(request, 'item/detail.html', {
        'item' : item,
        'related_items' : related_items,
    })



@login_required
def new(request):

    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', item_id=item.id)

    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form' : form,
        'title' : 'New item'
    })


@login_required
def edit(request, item_id):
    item = get_object_or_404(Item, pk=item_id, created_by=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', item_id=item.id)

    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form' : form,
        'title' : 'Edit item'
    })


@login_required
def delete(request, item_id):

    item = get_object_or_404(Item, pk=item_id, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')
