from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)
    full = models.CharField(max_length=200)   

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    pos = models.CharField(max_length=200)   
    degree = models.CharField(max_length=200)   
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
class Program(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)   
    descr = models.TextField()   
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    coord = models.CharField(max_length=200)
    coord_contact = models.CharField(max_length=200)   
    disc = models.TextField()

    def __str__(self):
        return self.name

class Home(models.Model):
    title = models.CharField(max_length=200)
    descr = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return self.title