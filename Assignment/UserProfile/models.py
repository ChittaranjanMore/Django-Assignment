##### Important  Modules for the  User Profile Moodels ################
from django.db import models
import datetime
from ckeditor.fields import RichTextField
########################################################################
# Create your models here.

year_dropdown = []
for y in range(2011, (datetime.datetime.now().year + 5)):
    year_dropdown.append((y, y))

BOOL_CHOICES = (('Yes',True), ( 'No',False))

###### Implementation of User Profile and EducationalDetails Models #######################

class EducationalDetails(models.Model):
    Id = models.AutoField(primary_key=True)    
    Degree = models.CharField(max_length=500,blank=True,null=True)
    YearOfPassing =  models.IntegerField(('year'),choices=year_dropdown, default=datetime.datetime.now().year)
    CertificateImage = models.BooleanField(choices=BOOL_CHOICES)

    def __str__(self):
        return self.Degree

class user_profile(models.Model):
    Id = models.AutoField(primary_key=True)    
    FullName = models.CharField(max_length=500,blank=True,null=True)
    ProfileImage = models.ImageField(blank=True,null=True,upload_to='images/')
    EmailId = models.EmailField(max_length = 254)
    ShortDescription = models.TextField(max_length=1000,blank=True,null=True)
    LongDescription = RichTextField(blank=True,null=True)
    EducationDetails = models.ForeignKey(EducationalDetails,on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.FullName

################################################################################################################