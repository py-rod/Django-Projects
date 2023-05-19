from django.db import models
import os
import random
import string
from django.utils import timezone
from django.template.defaultfilters import slugify
# Create your models here.


class Carousel(models.Model):
    def image_upload_to(self, instance):
        if instance:
            return os.path.join("Carousel", instance)
        return None

    image1 = models.ImageField(
        default="./Default/noimage.png", upload_to=image_upload_to, max_length=255)
    image2 = models.ImageField(
        default="./Default/noimage.png", upload_to=image_upload_to, max_length=255)
    image3 = models.ImageField(
        default="./Default/noimage.png", upload_to=image_upload_to, max_length=255)

    def __str__(self):
        return "Images"

    class Meta:
        verbose_name_plural = "Carousel"


class Categories(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    slug = models.SlugField(blank=False, unique=True, null=False)

    def save(self, *args, **kwargs):
        slug = "".join(random.sample(f"{string.ascii_letters}", 40))

        if Categories.objects.filter(slug=self.slug).exists() == True and self.slug != "":
            print("Este slug no esta recien creado y se guarda todo en el mismo")
            super().save(*args, **kwargs)

        if Categories.objects.filter(slug=slug).exists() == False and self.slug == "":
            print(
                "Este es un nuevo slug y esta recien creado. Y no existe en la base de datos")
            self.slug = slug
            super().save(*args, **kwargs)

        if Categories.objects.filter(slug=slug).exists() == True and self.slug == "":
            print(
                "Es un nuevo slug. Pero esta comprobando si extiste alguno en la base de datos")
            while True:
                slug = "".join(random.sample(f"{string.ascii_letters}", 40))
                if Categories.objects.filter(slug=slug).exists() == False and self.slug == "":
                    self.slug = slug
                    super().save(*args, **kwargs)
                    break

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "Categories"
        ordering = ("-id",)


class Products(models.Model):
    TAXES = (
        ("Include", "Include"),
        ("Not included", "Not included")
    )

    def image_upload_to(self, instance):
        if instance:
            return os.path.join("Products_Images", slugify(self.series.slug), slugify(self.product_slug), instance)
        return None

    name = models.CharField(max_length=200, blank=False, unique=False)
    image = models.ImageField(
        default="./Default/noproduct.jpg", upload_to=image_upload_to, max_length=255)
    series = models.ForeignKey(Categories, default="", blank=False,
                               help_text="Select the categorie of the product", on_delete=models.SET_DEFAULT)
    taxes = models.CharField(max_length=100, default="",
                             choices=TAXES, blank=False)
    brand = models.CharField(max_length=200, default="",
                             blank=True, help_text="Enter store brand")
    price = models.FloatField(blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    description = models.TextField(max_length=700, default="", blank=False)
    product_slug = models.SlugField(blank=False, unique=True, null=False)
    published = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        slug = "".join(random.sample(f"{string.ascii_letters}", 40))

        if Products.objects.filter(product_slug=self.product_slug).exists() == True and self.product_slug != "":
            print(self.product_slug)
            print("Este slug no esta recien creado y se guarda todo en el mismo")
            super().save(*args, **kwargs)

        if Products.objects.filter(product_slug=slug).exists() == False and self.product_slug == "":
            print(
                "Este es un nuevo slug y esta recien creado. Y no existe en la base de datos")
            self.product_slug = slug
            super().save(*args, **kwargs)

        if Products.objects.filter(product_slug=slug).exists() == True and self.product_slug == "":
            print(
                "Es un nuevo slug. Pero esta comprobando si extiste alguno en la base de datos")
            while True:
                slug = "".join(random.sample(f"{string.ascii_letters}", 40))
                if Products.objects.filter(product_slug=slug).exists() == False and self.product_slug == "":
                    self.product_slug = slug
                    super().save(*args, **kwargs)
                    break

    def __str__(self):
        return self.name

    def slug(self):
        return self.series.slug + "/" + self.product_slug

    class Meta:
        verbose_name_plural = "Products"
        db_table = "Products"
        ordering = ("-id",)
