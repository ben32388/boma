from .models import Page
from django import forms
class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ('name','url','folder','tags')