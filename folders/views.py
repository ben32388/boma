from django.shortcuts import get_object_or_404, redirect, render
from .models import Folder
from .forms import FolderForm
from pages.models import Page
from pages.forms import PageForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from taggit.models import Tag
from django.db.models import Q
@login_required
def index(request):
    folders = Folder.objects.filter(user_id=request.user.pk)
    folderform = FolderForm(request.POST or None)
    pages = Page.objects.filter(user_id=request.user.pk)
    pageform = PageForm(request.POST or None)
    username = request.user
    tags =[]
    if pages:
        for page in pages:
            tags += page.tags.all()
        tags = list(set(tags))
    if folderform.is_valid():
        f_form = folderform.save(commit=False)
        f_form.user_id = request.user.pk
        f_form.save()
        return redirect('index')
    if pageform.is_valid():
        p_form = pageform.save(commit=False)
        p_form.user_id = request.user.pk
        p_form.save()
        pageform.save_m2m()
        return redirect('index')
    id =request.GET.get('id','')
    title =request.GET.get('title','')
    if title:
        folder = get_object_or_404(Folder, pk=id,user_id=request.user.pk)
        folder.title=title
        folder.save()
        return redirect('index')

    q =request.GET.get('q','')
    if q:
        return redirect('/folders/?q='+q)
    return render(request,'home.html', {
        'tags' : tags,'username' : username, 'folders' : folders, 'pages' : pages, 'folderform' : folderform, 'pageform' : pageform,
    })
@login_required
def folder_delete(request,pk):
    folder = get_object_or_404(Folder, pk=pk,user_id=request.user.pk)
    folder.delete()
    return redirect('index')


@login_required
def page_show(request,pk):
    folders = Folder.objects.filter(user_id=request.user.pk)
    folder = get_object_or_404(Folder, pk=pk,user_id=request.user.pk)
    pages = Page.objects.filter(folder_id=pk,user_id=request.user.pk)
    pages_all = Page.objects.filter(user_id=request.user.pk)

    tags =[]
    if pages_all:
        for page in pages_all:
            tags += page.tags.all()
        tags = list(set(tags))
    id =request.GET.get('id','')
    pageform = None
    pageform_add = None
    if id:
        page = get_object_or_404(Page, pk=id)
        pageform = PageForm(request.POST or None,instance=page)
        if pageform.is_valid():
            pageform.save()
            return redirect('page_show',pk=pk)
    else:
        pageform_add = PageForm(request.POST or None)
        if pageform_add.is_valid():
            p_form = pageform_add.save(commit=False)
            p_form.user_id = request.user.pk
            p_form.save()
            pageform_add.save_m2m()
            return redirect('page_show',pk=pk)
    q =request.GET.get('q','')
    if q:
        return redirect('/folders/?q='+q)
    return render(request,'content.html', {
        'tags' : tags, 'folders' : folders, 'pages' : pages, 'folder' : folder, 'pageform' : pageform, 'pageform_add' : pageform_add,
    })

@login_required
def page_delete(request,fpk,pk):
    page = get_object_or_404(Page, pk=pk,user_id=request.user.pk)
    page.delete()
    # return HttpResponseRedirect(next)
    return redirect('../../../')

@login_required
def tag_show(request,pk):
    folders = Folder.objects.filter(user_id=request.user.pk)
    # folder = get_object_or_404(Folder, pk=pk,user_id=request.user.pk)
    tag = get_object_or_404(Tag, id=pk)
    pages = Page.objects.filter(tags=tag,user_id=request.user.pk)
    # pages = Page.objects.filter(folder_id=pk,user_id=request.user.pk)
    pages_all = Page.objects.filter(user_id=request.user.pk)
    
    tags =[]
    if pages_all:
        for page in pages_all:
            tags += page.tags.all()
        tags = list(set(tags))
    id =request.GET.get('id','')
    pageform = None
    pageform_add = None
    if id:
        page = get_object_or_404(Page, pk=id)
        pageform = PageForm(request.POST or None,instance=page)
        if pageform.is_valid():
            pageform.save()
            return redirect('tag_show',pk=pk)
    else:
        pageform_add = PageForm(request.POST or None)
        if pageform_add.is_valid():
            p_form = pageform_add.save(commit=False)
            p_form.user_id = request.user.pk
            p_form.save()
            pageform_add.save_m2m()
            return redirect('tag_show',pk=pk)
    q =request.GET.get('q','')
    if q:
        return redirect('/folders/?q='+q)
    return render(request,'content.html', {
        'tags' : tags, 'folders' : folders, 'pages' : pages, 'folder' : tag, 'pageform' : pageform, 'pageform_add' : pageform_add,
    })

@login_required
def tag_page_delete(request,tpk,pk):
    page = get_object_or_404(Page, pk=pk,user_id=request.user.pk)
    page.delete()
    # return HttpResponseRedirect(next)
    return redirect('../../../')

@login_required
def search(request):
    q =request.GET.get('q','')
    pages= None
    if q:
        pages = Page.objects.filter(
            Q(name__icontains=q)

        )

    folders = Folder.objects.filter(user_id=request.user.pk)
    folder = "搜尋 : "+q
    # pages = Page.objects.filter(folder_id=pk,user_id=request.user.pk)
    pages_all = Page.objects.filter(user_id=request.user.pk)

    tags =[]
    if pages_all:
        for page in pages_all:
            tags += page.tags.all()
        tags = list(set(tags))
    id =request.GET.get('id','')
    pageform = None
    pageform_add = None
    if id:
        page = get_object_or_404(Page, pk=id)
        pageform = PageForm(request.POST or None,instance=page)
        if pageform.is_valid():
            pageform.save()
            return redirect('/folders/?q='+q)
    else:
        folder_id =None
        pageform_add = PageForm(request.POST or None)
        if pageform_add.is_valid():
            p_form = pageform_add.save(commit=False)
            p_form.user_id = request.user.pk
            folder_id = p_form.folder_id
            p_form.save()
            pageform_add.save_m2m()
            return redirect('page_show',pk=folder_id)
    if not q and not id:
        return redirect('index')
    return render(request,'content.html', {
        'tags' : tags, 'folders' : folders, 'pages' : pages, 'folder' : folder, 'pageform' : pageform, 'pageform_add' : pageform_add,'q' : q,
    })

@login_required
def search_delete(request,pk):
    q =request.GET.get('q','')
    page = get_object_or_404(Page, pk=pk,user_id=request.user.pk)
    page.delete()
    # return HttpResponseRedirect(next)
    return redirect('/folders/?q='+q)
