from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-name', 'id': 'name', 'placeholder': 'Имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-name', 'id': 'email', 'placeholder': 'Email'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-subject', 'id': 'subject', 'placeholder': 'Тема'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-textarea', 'id': 'body', 'placeholder': 'Сообщение'}))