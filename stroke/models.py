from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.
class StrokeData(models.Model):
    age = models.IntegerField()
    hypertension = models.IntegerField()
    heartdisease = models.IntegerField()
    avgglucoselevel = models.IntegerField()
    bmi = models.IntegerField()
    genderMale = models.IntegerField()
    genderOther = models.IntegerField()
    evermarriedYes = models.IntegerField()
    worktypeNeverworked = models.IntegerField()
    worktypePrivate = models.IntegerField()
    worktypeSelfemployed = models.IntegerField()
    worktypechildren = models.IntegerField()
    ResidencetypeUrban = models.IntegerField()
    smokingstatusformerlysmoked = models.IntegerField()
    smokingstatusneversmoked = models.IntegerField()
    smokingstatussmokes = models.IntegerField()
    owner = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , related_name='owner' , null=True)
    date = models.DateField(auto_now_add=True)
    probability = models.FloatField(null=True)

    def __str__(self):
        return '{} {}'.format(self.owner , self.pk)


class DoctorHospital(models.Model):
    doctor_name = models.CharField(max_length=25)
    hospital_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_no = models.IntegerField()
    Location = models.CharField(max_length=25)
