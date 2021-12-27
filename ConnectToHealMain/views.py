from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .forms import *

def home(request):
    return render(request,"ConnectToHealMain/home.html")

def contact(request):
    return render(request,"ConnectToHealMain/contact.html")

def viewBlogs(request):
    blogs = BlogModel.objects.all()
    return render(request,"ConnectToHealMain/viewBlogs.html",{'blogs':blogs})

def ventingSpace(request):
    form = DiscussionForm()
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():            
            form.save()
    forums = DiscussionModel.objects.all()
    return render(request, 'ConnectToHealMain/ventingSpace.html', {'form': form,'forums':forums})

@login_required
def viewTherapists(request):
    therapists = TherapistModel.objects.all()
    if request.method =='POST':
        therapist = TherapistModel.objects.get(username=request.POST.get('therapistName'))
        return redirect("/detailAppointment/?username="+therapist.username)
    return render(request,"ConnectToHealMain/viewTherapists.html",{'therapists':therapists})

@login_required
def detailAppointment(request):
    therapistName = request.GET.get('username')
    form = BookAppointmentForm()
    if request.method=='POST':
        form = BookAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.therapistName = therapistName
            appointment.Uploader_info = request.user
            appointment.save()
            messages.success(request,"Appointment for {0} booked successfully! Thank you{1}".format(therapistName,request.user.userprofile.username))
            return redirect('ConnectToHeal-home')
        else:
            messages.error(request,"Failed to book appointment")
            return redirect('ConnectToHeal-home')
    return render(request,"ConnectToHealMain/detailAppointment.html",{'form':form})
    
@login_required      
def myAppointments(request):
    appointments = BookAppointmentModel.objects.filter(user = request.user)
    return render(request,"ConnectToHealMain/myAppointments.html",{'appointments':appointments})

@user_passes_test(lambda u:u.is_superuser)
def approveSessions(request):
    sessions = BookAppointmentModel.objects.filter()
    l=list(sessions)
    if request.method=="POST":
        session = request.POST.get('index')
        obj= BookAppointmentModel.objects.get(pk=session)
        obj.sessionstatus =True
        obj.save()
        messages.success(request,"Approved the request")
        return redirect("ConnectToHeal-approveSessions")
    return render(request, "ConnectToHealMain/approveSessions.html",{'sessions':sessions})