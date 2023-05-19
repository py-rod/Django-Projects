from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("<series>/", views.categorie, name="categorie"),
    path("<series>/<product>", views.product, name="product"),


    # VIEW ALL RECENT PRODUCTS
    path("recent-products",
         views.view_all_recent_product, name="all-recent"),

    # VIEW ALL PRODUCTS
    path("all-products", views.view_all_products, name="all-products")

]
