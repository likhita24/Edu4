from django.db import models

# Create your models here.
class application(models.Model):
    Full_Name = models.CharField(max_length=150)
    Emailaddress = models.EmailField(max_length=100)
    phone = models.IntegerField(blank=False)
    Address = models.CharField(max_length=200)
    Country = models.CharField(max_length=50)
    University_or_College = models.CharField(max_length=100)
    Year_of_study = models.IntegerField()
    Transcript = models.FileField(blank=False)
    Sop = models.FileField(blank=False)

    def __str__(self):
        return self.Full_Name



