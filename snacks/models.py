from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse 
class Snack (models.Model):
    title=models.CharField(max_length=64,default='snacks')
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    discreption=models.TextField(default="apple")

    def __str__(self) -> str:
        return self.title

    class Mate:
        verbose_name_plural='snacks'
        ordering=['-pk']

    def get_absolute_url(self):
        return reverse('SnackList',args=[self.id])