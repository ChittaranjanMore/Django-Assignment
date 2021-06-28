### important Modules ############
from django.urls import path
from . import views
from django.conf.urls import url
######################################


### Urls to map with main app urls #############################################
urlpatterns =[
    url("user_profile/",views.UserProfileView),
    path("userDetails/",views.UserProfileAndEducationalDetailsAPIView.as_view())
]
##################################################################################