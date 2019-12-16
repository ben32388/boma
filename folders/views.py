from django.shortcuts import render
from .models import Folder
from .forms import FolderForm
def folder_show(request):
    folder = Folder.objects.filter(user_id=request.user.pk)
    form = FolderForm(request.POST or None)
    if form.is_valid():
        planar = form.save(commit=False)
        planar.user_id = request.user.pk
        planar.save()
    return render(request,'home.html', {
        'folder' : folder, 'form' : form,
    })