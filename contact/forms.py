from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    # posso modificar campos de formulários usando widgets. Vamos ver aqui algumas formas de fazer isso:
    # Uma delas é criando campos no form, inclusive pode criar um campo existente de novo:
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Escreva seu nome',
            }),
        label="Nome",
        help_text="Texto de ajuda para seu usuario",
    )

    # Outra forma é editando o init da classe, como fiz a seguir (como só pode usar uma das forma eu
    # comentei duas:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Escreva seu nome'
        #})

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category',)
        # Uma terceira forma é configurando a classe meta como abaixo. Eu escolhi a primeira.
        # widgets = {'firs_name':forms.TextInput(
        #     attrs={
        #         'class': 'classe-a classe-b',
        #         'placeholder': 'Escreva seu nome',
        #            })
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError('Você digitou dois valores iguais', code='Invalid')

            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error('first_name', ValidationError('o valor digitado não é permitido', code='invalid'))
        return first_name
