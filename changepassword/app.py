from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, get_object_or_404

def changepassword(request):
    current_user = request.user
    if request.method == 'POST':
        currentpassword = request.POST.get('currentpassword')
        newpassword = request.POST.get('newpassword')
        confpassword = request.POST.get('confpassword')
        
        checking = check_password(currentpassword,current_user.password)
        if checking:
            if newpassword == confpassword:
                current_user.set_password(newpassword)
                current_user.save()           
                update_session_auth_hash(request,current_user)
                return redirect('profilepage')
    
    return render(request,'common/changepassword.html')