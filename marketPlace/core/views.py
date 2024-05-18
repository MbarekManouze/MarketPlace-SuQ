from django.shortcuts import render, redirect
from django.contrib.auth import logout
from item.models import Item, Category
from .forms import SignupForm


# Create your views here.

def Terms_of_use(request):
    return render(request, 'core/Terms.html')

def Privacy_Policy(request):
    return render(request, 'core/Privacy.html')

def About(request):
    return render(request, "core/About.html")

def logout_view(request):
    logout(request)
    return redirect('core:index')


def index(request):

    items = Item.objects.filter(is_sold=False)[:]
    categories = Category.objects.all()

    # for item in items:
    #     print(item.image)

    return render(request, 'core/index.html', {
        'categories': categories,
        'items' : items,
    })

def contact(request):
    return (render(request, 'core/contact.html'))


def Signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')

    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })