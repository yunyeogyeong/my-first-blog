from django.db import models
from django.utils import timezone



class Friend(models.Model):
    friend_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=50, blank=True, null=True)
    memo = models.CharField(max_length=10, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.friend_name