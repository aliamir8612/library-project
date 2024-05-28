from django.db import models

class category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 250, verbose_name = 'نام دسته بندی')
    def __str__ (self):
        return self.name

class book(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 250, verbose_name = 'نام کتاب')
    Author = models.CharField(max_length = 150, verbose_name = 'نویسنده')
    category = models.ForeignKey(category, on_delete = models.CASCADE, verbose_name = 'دسته بندی')
    publisher = models.CharField(max_length = 150, verbose_name = 'انتشارات')
    isBorrowing = models.BooleanField(default= False, verbose_name = 'قرض گرفته شده؟')
    def __str__ (self):
        return self.name
    

    
# Create your models here.