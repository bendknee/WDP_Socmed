from django.db import models

class Add_Friend(models.Model):
    name = models.CharField(max_length=27)
    url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
