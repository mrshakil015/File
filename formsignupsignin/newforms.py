from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from jobPortalApp.models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = PortalUserModel
        fields = ['username','UserType','Gender','City','ProfilePicture']
        
        help_texts = {
            'username':None
        }
        
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = PortalUserModel
        fields = ['username','password']