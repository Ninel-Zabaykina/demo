from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Portal(models.Model):
    STATUS = (
        ('решена', 'Решена'),
        ('отклонена', 'Отклонена'),
    )
