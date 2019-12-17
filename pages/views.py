from django.shortcuts import render
from .models import Page
from .forms import PageForm
from django.contrib.auth.decorators import login_required
@login_required
def page_show(request):
    # pages 為陣列
    pages = Page.objects.filter(user_id=request.user.pk)
    # 第一筆資料所有tag中的第一筆的id
    print(pages[0].tags.all()[0].id)
    form = PageForm(request.POST or None)
    if form.is_valid():
        planar = form.save(commit=False)
        planar.user_id = request.user.pk
        planar.save()
        form.save_m2m()
    return render(request,'home.html', {
        'pages' : pages, 'form' : form,
    })