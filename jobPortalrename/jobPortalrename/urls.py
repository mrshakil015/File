from django.contrib import admin
from django.urls import path
from jobPortalApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',browsejob,name="browsejob"),
    path('signinPage/',signinPage,name="signinPage"),
    path('signupPage/',signupPage,name="signupPage"),
    path('logoutpage/',logoutpage,name="logoutpage"),
    
    path('profilepage/',profilepage,name="profilepage"),
    path('editprofile/',editprofile,name="editprofile"),
    path('changepassword/',changepassword,name="changepassword"),
    
    path('postedjob/',postedjob,name="postedjob"),
    path('addjob/',addjob,name="addjob"),
    path('applyjob/<str:myid>',applyjob,name="applyjob"),
    path('editjob/<str:myid>',editjob,name="editjob"),
    path('deletejob/<str:myid>',deletejob,name="deletejob"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
