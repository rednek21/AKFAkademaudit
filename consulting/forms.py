from django import forms

from consulting.models import Contact


class LetsTalkForm(forms.Form):
    name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя', 'class': 'form-control', 'type': 'text', 'autocomplete': 'off'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите email', 'class': 'form-control', 'type': 'email', 'autocomplete': 'off'
    }))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Введите телефон', 'class': 'form-control', 'type': 'text', 'autocomplete': 'off'
    }))

    class Meta:
        fields = ('name', 'email', 'phone_number')


class IndexForm(forms.Form):
    name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя', 'class': 'form-control', 'type': 'text', 'autocomplete': 'off'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите email', 'class': 'form-control', 'type': 'email', 'autocomplete': 'off'
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Введите сообщение', 'class': 'form-control', 'type': 'text',
        'style': 'font-size: 16px;', 'autocomplete': 'off'
    }))

    class Meta:
        fields = ('name', 'email', 'text')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя', 'class': 'form-control', 'type': 'text', 'autocomplete': 'off'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите email', 'class': 'form-control', 'type': 'email', 'autocomplete': 'off'
    }))
    subject = forms.CharField(max_length=128, widget=forms.TextInput(attrs={
        'placeholder': 'Введите тему', 'class': 'form-control', 'type': 'text', 'autocomplete': 'off'
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Введите сообщение', 'class': 'form-control', 'type': 'text',
        'style': 'font-size: 16px;', 'autocomplete': 'off'
    }))

    class Meta:
        fields = ('name', 'email', 'subject', 'text')
