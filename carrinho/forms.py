from django import forms
from django.conf import settings

MAXIMO_PRODUTOS = [
    (i, str(i)) for i in range(1, settings.MAXIMO_PRODUTOS + 1)
]


class CarrinhoAddProdutoForm(forms.Form):
    quantidade = forms.TypedChoiceField(
        label="Quantidade", choices=MAXIMO_PRODUTOS, coerce=int
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )