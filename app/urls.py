from django.urls import path,include
from .views import *
urlpatterns = [ path("",indexpage,name="index"),
   path("index1/",indexpage1,name="index1"),
   path("signup/",singupage,name="signup"),
   path("register/",registeruser,name="register"),
   path("otppage/",otppage,name="otppage"),
   path("otp/",otpverify,name="otpverify"),
   path("loginpage/",loginpage,name="loginpage"),
   path("loginuser/",loginuser,name="login"),
   path("profile/<int:pk>",profilepage,name="profile"),
   path("updateprofie/<int:pk>",updateprofile,name="updateprofile"),
   path("joblist/",candidatejoblistpage,name="joblist"),
   path("apply/<int:pk>",applypage,name="apply"),
   path("applyjob/<int:pk>",applyjob,name="applyjob"),
   path("candidatelogout/",candidatelogout,name="candidatelogout"),



   ####################Company Side###############

   path("companyindex/",companyindexpage,name="companyindexpage"),
   path("companyprofilepage/<int:pk>",companyprofilepage,name="companyprofile"),
   path("updatecompanyprofile/<int:pk>",updatecompanyprofile,name="updatecompanyprofile"),
   path("jobpostpage/",jobpostpage,name="jobpostpage"),
   path("jobpost/",jobdetailssubmit,name="jobpost"),
   path("jobpostlist/",joblistpage,name="jobpostlist"),
   path("companylogout/",companylogout,name="companylogout"),
   path("applyjoblist/",jobapplylist,name="applylist"),


   ##################### ADMIN SIDE ##################
   path("adminloginpage/",AdminLoginPage,name="adminloginpage"),
   path("adminindex/",adminindexpage,name="adminindex"),
   path("adminlogin/",adminlogin,name="adminlogin"),
   path("adminuserlist/",adminuserlist,name="userlist"),
   path("admincompanylist/",admincompanylist,name="companylist"),
   path("deleteuser/<int:pk>",userdelete,name="userdelete"),
   path("verifycompanypage/<int:pk>",verifycompanypage,name="verifycompanypage"),
   path("verifycompany/<int:pk>",verifycompany,name="verifycompany"),
   path("deletecompany/<int:pk>",companydelete,name="companydelete"),




]