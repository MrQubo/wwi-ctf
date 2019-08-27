from django.contrib.auth.models import User
from django.db import models


class Flag(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    flag = models.CharField(max_length=64)
    css = models.TextField()
    awaiting_check = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)

    class Meta:
        permissions = [("can_review", "can_review")]

    def __str__(self):
        return self.flag

    def get_id(self):
        print("pk", self.pk)
        return self.pk


class Favourite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE)