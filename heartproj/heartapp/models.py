from django.db import models

# Create your models here.
class ValueStore(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    age=models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    cp=models.IntegerField()
    trestbps=models.IntegerField()
    cholestrol=models.IntegerField()
    fbs=models.IntegerField()
    restecg=models.IntegerField()
    thalach=models.IntegerField()
    exang=models.IntegerField()
    oldpeak=models.IntegerField()
    slope=models.IntegerField()
    ca=models.IntegerField()
    thal=models.IntegerField()
    
    