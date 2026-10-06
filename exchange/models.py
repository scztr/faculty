from django.db import models
from django.utils import timezone
class ExchangeProgram(models.Model):

    language = models.CharField(max_length=200)
    places = models.IntegerField()
    deadline = models.DateField()
    descr = models.TextField()
    uni_name = models.CharField(max_length=200, default="")
    country = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.uni_name
    
    @property
    def is_open(self):
        return self.deadline >= timezone.localdate()