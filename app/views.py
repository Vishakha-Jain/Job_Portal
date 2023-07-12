
from django.shortcuts import render,redirect
from .models import*
from random import randint
# Create your views here.

def indexpage(request):
    return render(request,"app/index.html")

def indexpage1(request):
    return render(request,"app/index1.html")


def singupage(request):
    return render(request,"app/signup.html")

def registeruser(request):
    # we have made only one view for both candidate and compnay registration.
    # for candidate role
    if request.POST['role']=="candidate":
        role=request.POST['role']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        
        user=usermaster.objects.filter(email=email)
    
        if user:
            message="user already exists"
            return render(request,"app/signup.html",{'key1':message})
        elif(password==cpassword):
            otp=randint(100000,999999)
            newuser=usermaster.objects.create(role=role,otp=otp,email=email,password=password)
            newcand=candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
            return render(request,"app/otpverify.html",{'email':email})
        
    else:
        role=request.POST['role']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        
        user=usermaster.objects.filter(email=email)
    
        if user:
            message="user already exists"
            return render(request,"app/signup.html",{'key1':message})
        elif(password==cpassword):
            otp=randint(100000,999999)
            newuser=usermaster.objects.create(role=role,otp=otp,email=email,password=password)
            newcand=company.objects.create(user_id=newuser,firstname=fname,lastname=lname)
            return render(request,"app/otpverify.html",{'email':email})

def otppage(request):
    return render(request,"app/otpverify.html")


def otpverify(request):
    email=request.POST['email']
    otp=int(request.POST['otp']) 
    # otp is always in integer,hence we have type-casted it.

    user=usermaster.objects.get(email=email)
    # here we have to use get() method to get the email and otp too.

    if user:
        if user.otp==otp:
            message="otp verify successfully"
            return render(request,"app/login.html",{'message':message})
        else:
            message="otp is incorrect"
            return render(request,"app/otpverify.html",{'message':message})
        
    else:
        return render(request,"app/signup.html")
    
def loginpage(request):
    return render(request,"app/login.html")


def loginuser(request):
    if request.POST['role']=="candidate":
        email=request.POST['email']
        password=request.POST['password']
        user=usermaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="candidate":
                can=candidate.objects.get(user_id=user) #here we have to call the candidate table because it is having first name and last name.
                request.session['id']=user.id
                request.session['firstname']=can.firstname
                request.session['lastname']=can.lastname
                request.session['email']=user.email
                request.session['password']=user.password
                return redirect("index1")
            else:
                message="password does not match"
                return render(request,"app/login.html",{'msg':message})
            
        else:
            message="User does not exists"
            return render(request,"app/login.html",{'msg':message})
        
    if request.POST['role']=="company":
        email=request.POST['email']
        password=request.POST['password']
        user=usermaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="company":
                com=company.objects.get(user_id=user) #here we have to call the candidate table because it is having first name and last name.
                request.session['id']=user.id
                request.session['firstname']=com.firstname
                request.session['lastname']=com.lastname
                request.session['email']=user.email
                request.session['password']=user.password
                return redirect("companyindexpage")
            else:
                message="password does not match"
                return render(request,"app/login.html",{'msg':message})
            
        else:
            message="User does not exists"
            return render(request,"app/login.html",{'msg':message})
        
def profilepage(request,pk):
    user=usermaster.objects.get(pk=pk)
    can=candidate.objects.get(user_id=user)
    return render(request,"app/profile.html",{'user':user,'can':can})

def updateprofile(request,pk):
    user=usermaster.objects.get(pk=pk)
    if user.role=="candidate":
        can=candidate.objects.get(user_id=user)
        can.contact=request.POST['contact'] #first entry belongs to database field ,second entry belong to html input name
        can.state=request.POST['state']
        can.city=request.POST['city'] #always remember that only one side is having square brackets.
        can.address=request.POST['address']
        can.dob=request.POST['dob']
        can.gender=request.POST['gender']
        can.min_salary=request.POST['min_salary']
        can.max_salary=request.POST['max_salary']
        can.job_type=request.POST['job_type']
        can.jobcategory=request.POST['jobcategory']
        can.country=request.POST['country']
        can.highestedu=request.POST['highestedu']
        can.experience=request.POST['experience']
        can.website=request.POST['website']
        can.shift=request.POST['shift']
        can.jobdescription=request.POST['jobdescription']
        can.profile_pic=request.FILES['image']
        can.save()
        url=f"/profile/{pk}" #formatting url,formatting url is used when we have parameterized method and we have tocall in the views.
        return redirect(url)

def candidatejoblistpage(request):
    all_job=jobdetails.objects.all()
    return render(request,"app/job-list.html",{'all_job': all_job})


def applypage(request,pk):
    user=request.session['id']
    if user:
        cand=candidate.objects.get(user_id=user)
        job=jobdetails.objects.get(id=pk)
    return render(request,"app/apply.html",{'user':user,'cand':cand,'job':job})

def applyjob(request,pk):
    user=request.session['id']
    if user:
        can=candidate.objects.get(user_id=user)
        job=jobdetails.objects.get(id=pk)
        edu=request.POST['highestedu']
        experience=request.POST['experience']
        website=request.POST['website'] 
        min_salary=request.POST['min_salary']
        max_salary=request.POST['max_salary']
        gender=request.POST['gender']
        resume=request.FILES['C.V.']
        newapply=applicant.objects.create(candidate=can,job=job,education=edu,experience=experience,website=website,min_salary=min_salary,max_salary=max_salary,gender=gender,resume=resume)
        message="Job applied Successfully"
        return render(request,"app/apply.html",{'msg':message})


def candidatelogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('signup')





############################ Company Side #############################

def companyindexpage(request):
    return render(request,"app/company/index.html")


def companyprofilepage(request,pk):
    user=usermaster.objects.get(pk=pk)
    comp=company.objects.get(user_id=user)
    return render(request,"app/company/profile.html",{'user':user,'comp':comp})

def updatecompanyprofile(request,pk):
    user=usermaster.objects.get(pk=pk)
    if user.role=="company":
        comp=company.objects.get(user_id=user)
        comp.firstname=request.POST['firstname']
        comp.lastname=request.POST['lastname']
        comp.company_name=request.POST['company_name']
        comp.state=request.POST['email']
        comp.city=request.POST['website']
        comp.contact=request.POST['email']
        comp.website=request.POST['city']
        comp.description=request.POST['state']
        comp.address=request.POST['address']
        comp.logo_pic=request.FILES['img']
        comp.save()
        url=f'/companyprofilepage/{pk}'
        return redirect(url)
#in redirect argument we can use view name ,url name and url also by formatting.

def jobpostpage(request):
    return render(request,"app/company/jobpost.html")


def jobdetailssubmit(request):
    # when we have to use id of request.session in views we have to use it like this request.session['id'],but when we have to use same thing in template we have to use request.session.id;
    user=usermaster.objects.get(id=request.session['id'])
    if user.role == "company":
        comp=company.objects.get(user_id=user)
        jobname=request.POST['jobname']
        companyname=request.POST['companyname']
        companyaddress=request.POST['companyaddress']
        jobdescription=request.POST['jobdescription']
        qualification=request.POST['qualification']
        responsibilities=request.POST['responsibilities']
        location=request.POST['location']
        companywebsite=request.POST['companywebsite']
        companyemail=request.POST['companyemail']
        companycontact=request.POST['companycontact']
        salarypackage=request.POST['salarypackage']
        experience=request.POST['experience']
        logo=request.FILES['logo']
        newjob=jobdetails.objects.create(company_id=comp,jobname=jobname,companyname=companyname,companyaddress=companyaddress,jobdescription=jobdescription,qualification=qualification,responsibilities=responsibilities,location=location,companywebsite=companywebsite,companyemail=companyemail,companycontact=companycontact,salarypackage=salarypackage,experience=experience,logo=logo)
        message="Job Post Successfully"
        return render(request,"app/company/jobpost.html",{'message':message})
    

def joblistpage(request):
    all_job=jobdetails.objects.all()
    return render(request,"app/company/jobpostlist.html",{'all_job': all_job})

def jobapplylist(request):
    all_jobapply=applicant.objects.all()
    return render(request,"app/company/applyjoblist.html",{'all_job':all_jobapply}) 


def companylogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')


######################### ADMIN SIDE ###################

def AdminLoginPage(request):
    return render(request,"app/admin/login.html")

def adminindexpage(request):
    # this logic is used not directly open the index page first we have to login and then redirect to the index page
    if 'username' in request.session and 'password' in request.session: 
        return render(request,"app/admin/index.html")
    else:
        return redirect('adminloginpage')

def adminlogin(request):
    username=request.POST['uname']
    password=request.POST['password']
    if username=="admin" and password=="admin":
        request.session['username']=username
        request.session['password']=password
        return redirect('adminindex')
    else:
        message="user name and password does not match"
        return render(request,"app/admin/login.html",{'msg':message})


# difference between get and filter means get is used for fetching only one object with unique key.
# filter is used for obtaining objects having same value attribute.
# in get attribute we have to use primary key which is unique hence we get the one object.
def adminuserlist(request):
    all_user=usermaster.objects.filter(role="candidate")
    return render(request,"app/admin/userlist.html",{'all_user':all_user})

def admincompanylist(request):
    all_company=usermaster.objects.filter(role="company")
    return render(request,"app/admin/companylist.html",{'all_company':all_company})


def userdelete(request,pk):
    user=usermaster.objects.get(pk=pk)
    user.delete()
    return redirect('userlist')

def verifycompanypage(request,pk):
    company=usermaster.objects.get(pk=pk)
    if company:
        return render(request,"app/admin/verify.html",{'company':company})
    
def verifycompany(request,pk):
    company=usermaster.objects.get(pk=pk)
    if company:
        company.is_verified=request.POST['is_verified']
        company.save()
        return redirect("companylist")
    
def companydelete(request,pk):
    company=usermaster.objects.get(pk=pk)
    company.delete()
    return redirect('companylist')