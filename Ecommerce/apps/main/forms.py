from django import forms


class ProductFilterForm(forms.Form):

    PRICE_CHOICES = [
        (1, "1 - 100"),
        (2, "101 - 500"),
        (3, "501 - 1000"),
        (4, "1001 - 5000"),
        (5, "5001 o más"),
    ]
    ORDER_CHOICES = [
        ("name", "Nombre (A-Z)"),
        ("-name", "Nombre (Z-A)"),
        ("price", "Precio (menor a mayor)"),
        ("-price", "Precio (mayor a menor)"),
    ]

    price = forms.ChoiceField(choices=PRICE_CHOICES,
                              widget=forms.Select, required=False, label="Precio")
    order = forms.ChoiceField(choices=ORDER_CHOICES,
                              widget=forms.Select, label="Ordernar por")
