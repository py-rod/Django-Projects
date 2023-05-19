from django.shortcuts import render, redirect
from datetime import timedelta
from django.utils import timezone

from .models import Categories, Products, Carousel

from .forms import ProductFilterForm
# Create your views here.


def base(request):
    carousel = Carousel.objects.all()
    cate = Categories.objects.all().order_by("name")
    produ = Products.objects.all()

    date_now = timezone.now() - timedelta(days=30)
    recent_add_product = Products.objects.filter(published__gte=date_now)

    return render(request, "layouts/base.html", {
        "images": carousel,
        "categories": cate,
        "products": produ,
        "recents": recent_add_product
    })


def categorie(request, series):
    cate = Categories.objects.all().order_by("name")
    produ = Products.objects.filter(series__slug=series).all()
    return render(request, "categorie.html", {
        "categories": cate,
        "products": produ
    })


def product(request, series, product):
    produ = Products.objects.filter(
        series__slug=series, product_slug=product).first()
    return render(request, "product.html", {
        "product": produ
    })


def view_all_recent_product(request):
    cate = Categories.objects.all().order_by("name")

    date_now = timezone.now() - timedelta(days=30)
    recent_add_product = Products.objects.filter(published__gte=date_now)

    form = ProductFilterForm(request.GET)

    if form.is_valid():
        price = form.cleaned_data["price"]
        order = form.cleaned_data["order"]

        if price == "1":
            recent_add_product = recent_add_product.filter(
                price__range=(1, 100))
        elif price == "2":
            recent_add_product = recent_add_product.filter(
                price__range=(101, 500))
        elif price == "3":
            recent_add_product = recent_add_product.filter(
                price__range=(501, 1000))
        elif price == "4":
            recent_add_product = recent_add_product.filter(
                price__range=(1001, 5000))
        elif price == "5":
            recent_add_product = recent_add_product.filter(price__gte=5001)

        recent_add_product = recent_add_product.order_by(order)

    return render(request, "view-all-recent-product.html", {
        "form": form,
        "categories": cate,
        "recents": recent_add_product
    })


def view_all_products(request):
    cate = Categories.objects.all().order_by("name")
    produ = Products.objects.all()
    form = ProductFilterForm(request.GET)

    if form.is_valid():
        price = form.cleaned_data["price"]
        order = form.cleaned_data["order"]

        if price == "1":
            produ = produ.filter(price__range=(1, 100))
        elif price == "2":
            produ = produ.filter(price__range=(101, 500))
        elif price == "3":
            produ = produ.filter(price__range=(501, 1000))
        elif price == "4":
            produ = produ.filter(price__range=(1001, 5000))
        elif price == "5":
            produ = produ.filter(price__gte=5001)

        produ = produ.order_by(order)

    return render(request, "view-all-products.html", {
        "form": form,
        "categories": cate,
        "products": produ
    })
