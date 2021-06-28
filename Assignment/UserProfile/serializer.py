### Important Modules for serialize the class########
from rest_framework import serializers
from .models import user_profile,EducationalDetails
#####################################################

##### Serializer class for User Details ######################################
class UserProfileAndEducationalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_profile
        fields = '__all__'
        depth = 1
##################################################################################