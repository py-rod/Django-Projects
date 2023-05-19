from django.contrib import admin
from .models import Categories, Products, Carousel

# Register your models here.


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    fields = ["image1", "image2", "image3"]


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    fields = ["name",]
    list_display = ("name",)
    list_display_links = ("name",)
    list_per_page = 20
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = ["name", "image", "series", "brand", "taxes", "price",
              "stock", "description", "published"]
    list_display = ("name", "price", "taxes")
    list_display_links = ("name", "price", "taxes")
    list_filter = ("taxes", )
    list_per_page = 20
    search_fields = ("id", "name")
    ordering = ("-id",)
