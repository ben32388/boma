from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from folders.models import Folder


class Page(models.Model):
    name = models.CharField('名稱', max_length=50) 
    url = models.URLField(max_length = 200)
    tags = TaggableManager()
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, verbose_name='資料夾')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='使用者')

    
    def __str__(self):
        return self.name