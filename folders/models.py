from django.db import models
from django.contrib.auth.models import User


class Folder(models.Model):
    name = models.CharField('名稱', max_length=50) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='使用者')
    
    def __str__(self):
        return self.name
