from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=20)

class stud_Reg(models.Model):
    name=models.CharField(max_length=100)
    login_id=models.OneToOneField(login,on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin_code=models.IntegerField(max_length=100)
    password=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    role=models.CharField(max_length=20)

class teach_Reg(models.Model):
    name=models.CharField(max_length=100)
    login_id=models.OneToOneField(login,on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin_code=models.IntegerField(max_length=100)
    password=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    experience=models.IntegerField()
    role=models.CharField(max_length=20)
