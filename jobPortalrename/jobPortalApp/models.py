from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class PortalUserModel(AbstractUser):
    USERTYPE = [
        ('Recruiter','Recruiter'),
        ('JobSeeker','JobSeeker'),
    ]
    UserType = models.CharField(choices=USERTYPE, max_length = 50, null=True)
    City = models.CharField(max_length=50, null=True)
    GENDER=[
        ('Male','Male'),
        ('Female','Female'),
    ]
    Gender= models.CharField(choices=USERTYPE,max_length=50, null=True)
    ProfilePicture = models.ImageField(upload_to='media/profile',null=True)

class BasicInfoModel(models.Model):
    portaluser = models.OneToOneField(PortalUserModel, on_delete=models.CASCADE, related_name="basicinfomodel",null=True)
    Fathername = models.CharField(max_length=50, null=True)
    Mothername = models.CharField(max_length=50, null=True)
    DOB = models.DateField(null=True)
    STATUS = [
        ('Married','Married'),
        ('UnMarried','UnMarried'),
    ]
    MaritalStatus = models.CharField(choices=STATUS,max_length=50, null=True)

class ContactDetailsModel(models.Model):
    portaluser = models.OneToOneField(PortalUserModel, on_delete=models.CASCADE, related_name="contactinfomodel",null=True)
    Mobile = models.CharField(max_length=50, null=True)
    EmergencyContact = models.CharField(max_length=50, null=True)
    PresentAddress = models.CharField(max_length=100, null=True)
    PermanentAddress = models.CharField(max_length=100, null=True)

class EducationalModel(models.Model):
    portaluser = models.ForeignKey(PortalUserModel, on_delete=models.CASCADE, related_name="educationalinfomodel",null=True)
    Degree = models.CharField(max_length=50, null=True)
    PassingYear = models.CharField(max_length=50, null=True)
    Grade = models.CharField(max_length=50, null=True)
    Department = models.CharField(max_length=50, null=True)
    

class JobModel(models.Model):
    CreatedBy = models.ForeignKey(PortalUserModel, on_delete=models.CASCADE, related_name='job_models', null=True)
    job_title = models.CharField(max_length=100, null=True)
    company_description = models.CharField(max_length=100, null=True)
    company_logo = models.ImageField(upload_to='media/jobmodel', null=True)
    company_name = models.CharField(max_length=100, null=True)
    company_location = models.CharField(max_length=100, null=True)
    qualification =models.CharField(max_length=100, null=True)
    salary =models.CharField(max_length=100, null=True)
    deadline =models.DateField(null=True)
    
    def __str__(self):
        return self.job_title
    
class jobApplyModel(models.Model):
    applicant = models.ForeignKey(PortalUserModel,on_delete=models.CASCADE, related_name='applicantuser', null=True)
    job = models.ForeignKey(JobModel,on_delete=models.CASCADE, null=True)
    skills= models.CharField(max_length=100,null=True)
    qualification= models.CharField(max_length=100,null=True)
    profileimage= models.ImageField(upload_to='media/seeker_img',null=True)
    resume = models.FileField(upload_to='media/seeker_resume',null=True)
    status= models.CharField(max_length=100,default="Pending", null=True)
    
    def __str__(self):
        return self.applicant.username
