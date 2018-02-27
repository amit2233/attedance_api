from django.db import models
from django.contrib.auth import User

# Create your models here.



class User(models.Model):




class Lec1(models.Model):
    day=models.CharField(max_length=20)
    sname=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    present=models.NullBooleanField()



class Lec2(models.Model):
    day=models.CharField(max_length=20)
    sname=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    present=models.NullBooleanField()



class Lec3(models.Model):
    day=models.CharField(max_length=20)
    sname=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    present=models.NullBooleanField()


class Lec4(models.Model):
    day=models.CharField(max_length=20)
    sname=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    present=models.NullBooleanField()



class Lec5(models.Model):
    day=models.CharField(max_length=20)
    sname=models.ForeignKey('Subjects',on_delete=models.CASCADE)
    present=models.NullBooleanField()



class Subjects(models.Model):


    sname=models.CharField(max_length=20)
    present=models.IntegerField(max_value=None,min_value=None)
    total=models.IntegerField(max_value=None,min_value=None)


    def __str__(self):
        return "@{}".format(self.sname)
