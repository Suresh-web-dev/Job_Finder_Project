
from django.shortcuts import render,redirect
from .models import emplayee,job,sign,user_login

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.contrib.auth import login, authenticate


# Create your views here.

def home(request):
    return render(request,"home.html")


def post_form(request):
    if request.method=="POST":
        job_name=request.POST.get("job_name")
        job_description=request.POST.get("job_description")
        qualification=request.POST.get("qualification")
        skills=request.POST.get("skills")
        salary=request.POST.get("salary")
        job.objects.create(job_name=job_name,job_description=job_description,qualification=qualification,skills=skills,salary=salary)
        obj={"job_name":job_name,"job_description":job_description,"qualification":qualification,"skills":skills,"salary":salary}
        return render(request,"post_form.html",obj)
    return render(request,"post_form.html")
    
    
def jobs(request):
    all_datas=job.objects.all()
    obj={"all":all_datas}
    return render(request,"jobs.html",obj)


def search(request):
    if request.method=="POST":
        job_name=request.POST.get("job_name")
        if job.objects.filter(job_name=job_name).exists():
            all_data=job.objects.filter(job_name=job_name).values()
            obj={"all":all_data}
        else:
            obj={"error" : "Not Found"}
        return render(request,"jobs.html",obj)
    return render(request,"jobs.html")


def apply_form(request):
    if request.method=="POST":
        applied_job=request.POST.get("applied_job")
        name=request.POST.get("name")
        email=request.POST.get("email")
        phon_number=request.POST.get("phon_number")
        file = request.FILES.get("file")
        emplayee.objects.create(applied_job=applied_job,name=name,email=email,phon_number=phon_number,file=file)
        obj={"applied_job":applied_job,"name":name,"email":email,"phon_number":phon_number,"file":file}
        return render(request, "apply_form.html",obj) 
    return render(request, "apply_form.html") 


def apply_datas(request):
    all_datas=emplayee.objects.all()
    obj={"all":all_datas}
    return render(request,"apply_datas.html",obj)


def one(request,id):
    a=job.objects.get(id=id)
    x={"a":a}
    return render(request,"apply_form.html",x)


def admin_page(request):
    return render(request,"admin.html")


def delete(request,id):
    emplayee.objects.get(id=id).delete()
    return redirect(apply_datas)



def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect(signup_view)

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect(signup_view)

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        
        
        sign.objects.create(username=username,email=email,password1=password1,password2=password2)
        obj={"username":username,"email":email,"password1":password1,"password2":password2}
        return render(request,"home.html",obj)
    return render(request, 'signup.html')

        
def signup_datas(request):
    all_datas=sign.objects.all()
    obj={"all":all_datas}
    return render(request,"signup_datas.html",obj)



def login_view(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        
        user_login.objects.create(username=username,password=password)
        obj={"username":username,"password":password}
        if user is not None:
            login(request,user)
            return redirect(home)

        else:
            messages.error(request,"invalid username or password")
            return redirect(login_view)
    return render(request,"login.html")


def login_datas(request):
    all_datas=user_login.objects.all()
    obj={"all":all_datas}
    return render(request,"login_datas.html",obj)


def logout_view(request):
    logout(request)
    return redirect(login_view)


