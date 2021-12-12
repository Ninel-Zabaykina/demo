from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=200, help_text="Укажите категорию заявки")

    def __str__(self):
        return self.name


class Portal(models.Model):
    STATUS = (
        ('решена', 'Решена'),
        ('отклонена', 'Отклонена'),
        ('новая', 'Новая')
    )
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='app_portal', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS, default='Новая')
    categories = models.ManyToManyField(Categories, help_text="Укажите категорию заявки")
    photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, null=True)

    def __str__(self):
        return self.title
