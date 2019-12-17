from django.shortcuts import render
from .models import Folder
from .forms import FolderForm
from pages.models import Page
from pages.forms import PageForm
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    folders = Folder.objects.filter(user_id=request.user.pk)
    folderform = FolderForm(request.POST or None)
    pages = Page.objects.filter(user_id=request.user.pk)
    pageform = PageForm(request.POST or None)
    username = request.user
    if folderform.is_valid():
        f_form = folderform.save(commit=False)
        f_form.user_id = request.user.pk
        f_form.save()
    if pageform.is_valid():
        p_form = pageform.save(commit=False)
        p_form.user_id = request.user.pk
        p_form.save()
        pageform.save_m2m()
    return render(request,'home.html', {
        'username' : username, 'folders' : folders, 'pages' : pages, 'folderform' : folderform, 'pageform' : pageform,
    })