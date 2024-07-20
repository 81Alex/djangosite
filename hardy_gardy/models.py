from django.db import models


class Form(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return f'{self.username}: {self.user_id}'


