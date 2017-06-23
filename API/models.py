from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    owner = models.ForeignKey('auth.User', related_name='task', on_delete=models.CASCADE)
    Task_Name = models.CharField(max_length=150)
    Task_Details = models.TextField()
    Task_By = models.CharField(max_length=100)
    Task_creation_Date = models.DateField()
    Task_End_Date = models.DateField()
    Task_Type = models.CharField(max_length=100)




class Exercise(models.Model):
    owner = models.ForeignKey('auth.User', related_name='exercise', on_delete=models.CASCADE)
    Exercise_name = models.CharField(max_length=100)
    Start_date = models.DateField()
    End_date = models.DateField()
    Exercise_day = models.CharField(max_length=50)
    Exercise_sets = models.IntegerField()
    Set_repetion = models.IntegerField()

class Diet(models.Model):
    owner = models.ForeignKey('auth.User', related_name='diet', on_delete=models.CASCADE)
    Food_Name = models.TextField()
    Start_date = models.DateField()
    End_date = models.DateField()
    Diet_day = models.TextField()
    Diet_Time = models.TimeField()

class Expense(models.Model):
    owner = models.ForeignKey('auth.User', related_name='expense', on_delete=models.CASCADE)
    Amount = models.DecimalField()
    Amount_type = models.TextField()
    Borrower_or_Lender_Name = models.TextField()

# Create your models here.
