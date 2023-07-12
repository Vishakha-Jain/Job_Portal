from django.db import models

# Create your models here.
class usermaster(models.Model):
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    otp=models.IntegerField()  #in integer field and non-integer field we don't have to use the max+length attributes.
    role=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)  #flag
    is_verified=models.BooleanField(default=False)
    is_created=models.DateTimeField(auto_now_add=True)
    is_updated=models.DateTimeField(auto_now_add=True)


class candidate(models.Model):
    user_id=models.ForeignKey(usermaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    dob=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    min_salary=models.CharField(max_length=50)
    max_salary=models.CharField(max_length=50)
    job_type=models.CharField(max_length=150)
    jobcategory=models.CharField(max_length=150)
    country=models.CharField(max_length=150)
    highestedu=models.CharField(max_length=150)
    experience=models.BigIntegerField(default=10)
    website=models.CharField(max_length=150)
    shift=models.CharField(max_length=150)
    jobdescription=models.TextField()
    profile_pic=models.ImageField(upload_to="app/img/candidate")

class company(models.Model):
    user_id=models.ForeignKey(usermaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    company_name=models.CharField(max_length=150)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    website=models.CharField(max_length=150)
    description=models.TextField()
    address=models.CharField(max_length=150)
    logo_pic=models.ImageField(upload_to="app/img/company")

class jobdetails(models.Model):
    company_id=models.ForeignKey(company,on_delete=models.CASCADE)
    jobname=models.CharField(max_length=250)
    companyname=models.CharField(max_length=250)
    companyaddress=models.CharField(max_length=250)    
    jobdescription=models.TextField()
    qualification=models.CharField(max_length=250)
    responsibilities=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    companywebsite=models.CharField(max_length=250)
    companyemail=models.CharField(max_length=250)
    companycontact=models.CharField(max_length=20)
    salarypackage=models.CharField(max_length=250)
    experience=models.BigIntegerField()
    logo=models.ImageField(upload_to="app/img/jobpost")
    # we don't have to give any max_length in textfield and bigintegerfiled or integerfiled.


class applicant(models.Model):
    candidate=models.ForeignKey(candidate,on_delete=models.CASCADE)
    job=models.ForeignKey(jobdetails,on_delete=models.CASCADE)
    education=models.CharField(max_length=200)
    experience=models.BigIntegerField()#when you have migrate the table and add the another field ,and then applying command makemigrations give error for that we have to select 2 option and then write "default=0 or default="" ".
    website=models.CharField(max_length=200)
    min_salary=models.CharField(max_length=200)
    max_salary=models.CharField(max_length=200)
    gender=models.CharField(max_length=20)
    resume=models.FileField(upload_to="app/resume")