from django.db import models

class Subscriber(models.Model):

    email = models.EmailField(null=False,blank=False)
    user_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.user_name

    