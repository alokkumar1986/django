from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Highestqualification(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    qualification_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.qualification_name
    
class Colour(models.Model):
    color_name = models.CharField(max_length=100)
    def	__str__(self):
        return	self.color_name

class Flower(models.Model):
    flower_name = models.CharField(max_length=100)
    color = models.ForeignKey(Colour, on_delete=models.CASCADE)
    def	__str__(self):
        return	self.flower_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    def	__str__(self):
        return	self.subject_name
    
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject)
    def	__str__(self):
        return	self.student_name
    
    
