from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def singleblog(request):
    return render(request, 'singleblog.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def cart(request):
    return render(request, 'cart.html', {})


def category(request):
    return render(request, 'category.html', {})


def checkout(request):
    return render(request, 'checkout.html', {})


def confirmation(request):
    return render(request, 'confirmation.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def elements(request):
    return render(request, 'elements.html', {})


def login(request):
    return render(request, 'login.html', {})


def singleproduct(request):
    return render(request, 'singleproduct.html', {})


def tracking(request):
    return render(request, 'tracking.html', {})