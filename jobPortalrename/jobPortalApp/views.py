from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from jobPortalApp.models import *
from jobPortalApp.forms import *

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        usertype = request.POST.get('usertype')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        city = request.POST.get('city')
        profilepic = request.FILES.get('profile_picture')
        print("password: ",username, password)
        
        if password == confirm_password:
            user = PortalUserModel.objects.create_user(
                username = username,
                password = password,
                email = email,
                UserType = usertype,
                Gender = gender,
                City = city,
                ProfilePicture = profilepic,
            )
            user.save()
            BasicInfoModel.objects.create(portaluser=user)
            if usertype == 'Recruiter':
                ContactDetailsModel.objects.create(portaluser=user)
            return redirect('signinPage')
    
    return render(request,'common/signup.html')

def signinPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('profilepage')
        else:
            print("User not exist")
    return render(request,'common/signin.html')

def profilepage(request):
    
    return render(request,'common/profile.html')

def editprofile(request):
    
    
    return render(request,'common/editprofile.html')

def logoutpage(request):
    logout(request)
    return redirect('signinPage')

def browsejob(request):
    data = JobModel.objects.all()
    current_user= request.user

    jobdata = []
    if current_user.is_authenticated:
        userdata = get_object_or_404(PortalUserModel, username=current_user)
        for job in data:
            applied = jobApplyModel.objects.filter(job=job, applicant=userdata).exists()
            jobdata.append({
                'job':job,
                'applied':applied,
            })
        
    elif current_user.is_anonymous:
       for job in data:
            jobdata.append({
                'job':job,
                'applied':'False',
            })
    context = {
        'jobdata':jobdata
    }
    return render(request,'browsejob.html',context)

def addjob(request):
    current_user = request.user
    userdata = get_object_or_404(PortalUserModel, username = current_user)
    if request.method == 'POST':
        jobform = JobForm(request.POST,request.FILES)
        if jobform.is_valid():
            job = jobform.save(commit=False)
            job.CreatedBy = userdata
            job.save()
    else:
        jobform = JobForm()
    
    context = {
        'jobform':jobform
    }
    
    return render(request,'addjob.html',context)

def editjob(request, myid):
    
    jobdata = get_object_or_404(JobModel, id=myid)
    if request.method == 'POST':
        jobform = JobForm(request.POST, request.FILES,instance=jobdata)
        
        if jobform.is_valid():
            jobdata = jobform.save(commit=False)
            jobdata.CreatedBy = request.user
            jobdata.save()
            return redirect('browsejob')
    else:
        jobform = JobForm(instance=jobdata)
    
    context = {
        'jobform':jobform
    }
    
    return render(request, 'editjob.html',context)

def deletejob(request, myid):
    jobdata = get_object_or_404(JobModel, id=myid)
    jobdata.delete()
    return redirect('browsejob')

def postedjob(request):
    current_user = request.user
    current_usertype =request.user.UserType
    
    if current_usertype == 'Recruiter':
        jobdata = JobModel.objects.filter(CreatedBy=current_user)
    else:
        jobdata = JobModel.objects.all()
    
    context = {
        'jobdata':jobdata
    }
        
    
    return render(request,'postedjob.html',context)

def applyjob(request, myid):
    jobdata = get_object_or_404(JobModel, id=myid)
    
    if request.method == 'POST':
        applyform = ApplyJobForm(request.POST, request.FILES)
        if applyform.is_valid():
            formdata = applyform.save(commit=False)
            formdata.applicant = request.user
            formdata.job = jobdata
            formdata.save()
            return redirect('profilepage')
    else:
        applyform = ApplyJobForm()
        
    context = {
        'applyform':applyform,
        'jobdata':jobdata,
    }
    
    
    return render(request,'applyjob.html',context)

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