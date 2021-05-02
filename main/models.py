from django.db import models

# Create your models here.
class application(models.Model):
    Full_Name = models.CharField(max_length=150)
    Emailaddress = models.EmailField(max_length=100)
    phone = models.IntegerField()
    Address = models.CharField(max_length=200)
    Country = models.CharField(max_length=50)
    University_or_College = models.CharField(max_length=100)
    Year_of_study = models.IntegerField()
    Department = models.CharField(max_length=100)
    Expected_Graduation_Year = models.IntegerField()
    cgpa = models.DecimalField(decimal_places=2, max_digits=3)
    Transcript = models.FileField(upload_to='transcripts/')
    Sop = models.FileField(upload_to='SOPs/')

    def __str__(self):
        return self.Full_Name



