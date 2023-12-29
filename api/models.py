from django.db import models

# Create your models here.


class Cities(models.Model):
    city_name = models.CharField(max_length=60)
    province = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

