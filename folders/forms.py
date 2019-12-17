from .models import Folder
from django import forms
class FolderForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    
    class Meta:
        model = Folder
        fields = ('title',)