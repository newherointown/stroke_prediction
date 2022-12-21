import pickle
import pandas as pd
import numpy as np
from .forms import Parameters
from django.contrib import messages
from .models import StrokeData,DoctorHospital
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login 
from django.contrib.auth.decorators import login_required

# Create your views here.
with open('stroke/static/stroke_predection.pkl', 'rb') as file:
    model = pickle.load(file)

def quickpredict(request):  
    
    if request.method =='POST':

        form=Parameters(request.POST)
        if form.is_valid():
            age=form.cleaned_data['age']
            hypertension=form.cleaned_data['hypertension']
            heartdisease=form.cleaned_data['heartdisease']
            avgglucoselevel=form.cleaned_data['avgglucoselevel']
            bmi=form.cleaned_data['bmi']
            genderMale=form.cleaned_data['genderMale']
            genderOther=form.cleaned_data['genderOther']
            evermarriedYes=form.cleaned_data['evermarriedYes']
            worktypeNeverworked=form.cleaned_data['worktypeNeverworked']
            worktypePrivate=form.cleaned_data['worktypePrivate']
            worktypeSelfemployed=form.cleaned_data['worktypeSelfemployed']
            worktypechildren=form.cleaned_data['worktypechildren']
            ResidencetypeUrban=form.cleaned_data['ResidencetypeUrban']

            smokingstatusformerlysmoked=form.cleaned_data['smokingstatusformerlysmoked']
            smokingstatusneversmoked=form.cleaned_data['smokingstatusneversmoked']
            smokingstatussmokes=form.cleaned_data['smokingstatussmokes']
            output1 = model.predict(np.array(
                    [age,hypertension,heartdisease,avgglucoselevel,bmi,genderMale,genderOther,
                    evermarriedYes,worktypeNeverworked,worktypePrivate,worktypeSelfemployed,
                    worktypechildren,ResidencetypeUrban, smokingstatusformerlysmoked,
                    smokingstatusneversmoked, smokingstatussmokes]).reshape(1,-1))
            #print('-----------------------------------------')
            #print(output)
            output1=output1[0]
            return render(request , 'output.html' , {'output1':output1})
        else:
            print('The form was not valid.')
            return redirect('/')   
    else:
        form=Parameters()
        return render(request,'quickpredict.html',{'form':form})    
def index(request): #Directs the user to home page . Different for authenticated and non authenticated users.
    if request.user.is_authenticated:
        if request.method=='POST':
    
            form=Parameters(request.POST)

            if form.is_valid():
                age=form.cleaned_data['age']
                hypertension=form.cleaned_data['hypertension']
                heartdisease=form.cleaned_data['heartdisease']
                avgglucoselevel=form.cleaned_data['avgglucoselevel']
                bmi=form.cleaned_data['bmi']
                genderMale=form.cleaned_data['genderMale']
                genderOther=form.cleaned_data['genderOther']
                evermarriedYes=form.cleaned_data['evermarriedYes']
                worktypeNeverworked=form.cleaned_data['worktypeNeverworked']
                worktypePrivate=form.cleaned_data['worktypePrivate']
                worktypeSelfemployed=form.cleaned_data['worktypeSelfemployed']
                worktypechildren=form.cleaned_data['worktypechildren']
                ResidencetypeUrban=form.cleaned_data['ResidencetypeUrban']
                smokingstatusformerlysmoked=form.cleaned_data['smokingstatusformerlysmoked']
                smokingstatusneversmoked=form.cleaned_data['smokingstatusneversmoked']
                smokingstatussmokes=form.cleaned_data['smokingstatussmokes']
                output1 = model.predict(np.array(
                    [age,hypertension,heartdisease,avgglucoselevel,bmi,genderMale,genderOther,
                    evermarriedYes,worktypeNeverworked,worktypePrivate,worktypeSelfemployed,
                    worktypechildren,ResidencetypeUrban, smokingstatusformerlysmoked,
                    smokingstatusneversmoked, smokingstatussmokes]).reshape(1,-1))
                danger = 'high' if output1 == 1 else 'low'
                output1=output1[0]
                saved_data = StrokeData(age=age ,  # Saving to database
                hypertension = hypertension,
                heartdisease = heartdisease,
                avgglucoselevel = avgglucoselevel,
                bmi = bmi,
                genderMale = genderMale,
                genderOther = genderOther , 
                evermarriedYes = evermarriedYes , 
                worktypeNeverworked = worktypeNeverworked,
                worktypePrivate = worktypePrivate,
                worktypeSelfemployed = worktypeSelfemployed,
                worktypechildren = worktypechildren,
                ResidencetypeUrban = ResidencetypeUrban,
                smokingstatusformerlysmoked = smokingstatusformerlysmoked,
                smokingstatusneversmoked = smokingstatusneversmoked,
                smokingstatussmokes = smokingstatussmokes,
                owner = request.user,
                probability = output1
                )  #Saved the authenticated users data in the database.
                saved_data.save()
                return render(request , 'output2.html',{'output1':output1 , 'danger':danger})


        form = Parameters()
        return render(request , 'user.html', {'form':form})
    return render(request , 'index.html')

def record(request): #Diplays previous record of authenticated user
    if request.user.is_authenticated:
        record_data = StrokeData.objects.filter(owner = request.user) #Filter only those data whose owner is the logged in user
        return render(request , 'record.html' , {'record_data':record_data})
    return redirect('/')
def heartdetail(request): # Displays previous results in detail
    if request.user.is_authenticated:
        record_data = StrokeData.objects.filter(owner = request.user)
        return render(request , 'heartdetail.html' , {'record_data':record_data})
    return redirect('/')
def symptoms(request): # Diplays list of symptoms of heart disease
    if request.user.is_authenticated:
        record_data = StrokeData.objects.all()
        return render(request , 'symptoms.html')
    return redirect('/')
def prevention(request): # Diplays list of prevention of heart disease
    if request.user.is_authenticated:
        return render(request , 'prevention.html')
    return render('/')
def doctorhospital(request): # Displays list of doctors and hospitals for user
    if request.user.is_authenticated:
        datas = DoctorHospital.objects.all()
        return render(request , 'doctorshospitals.html',{'datas':datas})
    return render('/')

def contact(request): #Diplays contact page . Sends email to HDPS using SMTP.
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title1')
        message = request.POST.get('message')        
        send_mail(title , message+'\n'+'From : '+name+'\n'+'Email : '+email ,from_email=email, recipient_list=['focusus1@gmail.com']) #Sends mail to HDPS
    return render(request , 'contact.html')



def about(request): #Displays about us page.
    return render(request , 'about.html')


def signin(request): # For the user to sign in.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'Invalid Credentials')
            return redirect('signin')
    else:
        return render(request,'signin.html')

def signup(request): #For the user to resister or sign up.
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, password=password,email=email,first_name = first_name,last_name=last_name)
            
            user.save()
            
            messages.success(request,f"User {username} created!")
            return redirect('signin')
        #return redirect('/')
    else:   
        return render(request,'signup.html')


def signout(request): # In order to logout from the website
    auth.logout(request)
    return redirect('/')       




