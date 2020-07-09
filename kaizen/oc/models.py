from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=256,default="")
    email=models.EmailField(default="")
    phone_no=models.CharField(max_length=256,default="")
    description=models.TextField(default="")
    def __str__(self):
        return self.name
#name #class #fathersname #school #phone_no #lastclasspercent #email #kidharse
class StudentDetail(models.Model):
    name=models.CharField(max_length=256,default="")
    email=models.EmailField(default="")
    phone_no=models.CharField(max_length=256,default="")
    fathers_name=models.CharField(max_length=256,default="")
    school=models.CharField(max_length=256,default="")
    lastclasspercent=models.CharField(max_length=256,default="")
    From_where_you_came_to_know_about_us=models.CharField(max_length=20)
    def __str__(self):
        return self.name

