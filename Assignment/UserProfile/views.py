
##### Important Modules #############################
from django.shortcuts import render
from .models import user_profile,EducationalDetails,BOOL_CHOICES
from django.http import HttpResponse
import re
import datetime
from ckeditor.fields import RichTextField
from .serializer import UserProfileAndEducationalDetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json
######################################################################
# Create your views here.


year = []
for y in range(2011, (datetime.datetime.now().year + 5)):
    year.append(y)

certificateImage = ('Yes','No')
BOOL_CHOICES = dict(BOOL_CHOICES)
longDescription = RichTextField()
APIUrl = 'http://127.0.0.1:8000/user/userDetails/'

############## Receiving data  from API ###########################################
def getAPIJson():
    apiResponse = requests.get(APIUrl)
    if apiResponse.status_code == 200:
        data = apiResponse.json()
    return data
########################################################################################

#############  Function to Insert data in the Database ###############################################
def UserProfileView(request):
    regex = '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
    user = user_profile()
    educationDetails = EducationalDetails()
    if request.method == "POST":
        educationDetails.Degree = request.POST["Degree"]
        educationDetails.YearOfPassing = request.POST["YearOfPassing"]
        educationDetails.CertificateImage = BOOL_CHOICES.get(request.POST["CertificateImage"])
        educationDetails.save()
        user.FullName = request.POST["FullName"]
        user.ProfileImage = request.FILES["ProfileImage"]
        user.EmailId = request.POST["EmailId"]
        user.ShortDescription = request.POST["ShortDescription"]
        user.LongDescription = request.POST["LongDescription"]
        user.EducationDetails = educationDetails
        user.save()
    
    ## getting the Received json data and shown on Page ###     
    data = getAPIJson()
    return render(request,'userprofile.html',{'year':year,'certificate':certificateImage,'data':data})
    
##################################################################################################################################

######################## written the Get API View Class to fetch all the User Details ###########################################
class UserProfileAndEducationalDetailsAPIView(APIView):
    serializer_class = UserProfileAndEducationalDetailsSerializer

    def get_queryset(self):
        userDetails = user_profile.objects.all()
        return userDetails

    def get(self,request,*args,**kwargs):
        userDetails = user_profile.objects.all()
        serializer = UserProfileAndEducationalDetailsSerializer(userDetails,many=True)
        return Response(serializer.data)    

#####################################################################################################################################