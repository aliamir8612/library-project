from django.db import models


class character(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 50, verbose_name = 'نام نقش')
    def __str__ (self):
        return self.name


class member(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 200, verbose_name = 'نام عضو')
    age = models.IntegerField(verbose_name = 'سن')
    character = models.ForeignKey(character, on_delete = models.CASCADE, verbose_name = 'نقش')
    libId = models.IntegerField(verbose_name = 'شماره عضویت کتابخانه')
    def __str__ (self):
        return self.name







# Create your models here.