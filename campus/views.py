from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    return render(request, "index.html")

def logout(request):
    auth.logout(request)
    messages.success(request, "You have logout! want to login again?")
    return redirect('login')

def logout_user(request):
    auth.logout(request)
    messages.success(request, "You have logout! want to login again?")
    return redirect('user-login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_superuser == True:
                auth.login(request, user)
                messages.success(request, "Login successful...")
                return redirect("dashboard")
            else:
                messages.error(request, "You are not allowed to access this page!")
                return redirect("login")
        else:
            messages.error(request, "Invalid Login details!")
            return redirect("login")
    return render(request, "login.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login successful...")
            return redirect("user-dashboard")
        else:
            messages.error(request, "Invalid Login details!")
            return redirect("user-login")
    return render(request, "user_login.html")

def dashboard(request):
    return render(request, "dashboard.html")

def user_dashboard(request):
    return render(request, "user_dashboard.html")

def user_report(request):
    if request.method == 'POST':
        title = request.POST['title']
        report = request.POST['report']
        report_date = request.POST['reportDate']

        new_report = Report.objects.create(
            title=title, report=report, report_date=report_date
        )
        new_report.save()
        messages.success(request, "Report added successful...")
        return redirect('user-report')
    return render(request, "user_report.html")

def about(request):
    user = User.objects.get(username=request.user)
    return render(request, "about.html", {'user': user})

def visitors(request):
    visitors = Visitor.objects.all()
    if request.method == 'POST':
        fullname = request.POST['fullName']
        phone = request.POST['phone']
        gender = request.POST['gender']
        dov = request.POST['visitDate']

        new_visitor = Visitor.objects.create(
            fullname=fullname, phone=phone, gender=gender,
            dov=dov
        )
        new_visitor.save()
        messages.success(request, "Visitor add successfully....")
        return redirect('visitors')
    return render(request, "visitors.html", {'visitors': visitors})

def report(request):
    reports = AdminReport.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        report = request.POST['report']
        report_date = request.POST['reportDate']

        new_report = AdminReport.objects.create(
            title=title, report=report, report_date=report_date
        )
        new_report.save()
        messages.success(request, "Report added successful...")
    return render(request, "reports.html", {'reports': reports})

def delete(request, id):
    report = AdminReport.objects.get(id=id)
    report.delete()
    messages.success(request, "Report deleted..")
    return redirect('reports')

def vehicles(request):
    vehicle = Vehicle.objects.all()
    if request.method == 'POST':
        veh_model = request.POST['model']
        number = request.POST['number']
        veh_color = request.POST['color']

        new_veh = Vehicle.objects.create(
            veh_model=veh_model, number=number, veh_color=veh_color
        )
        new_veh.save()
        messages.success(request, "Vehicle added successful...")
        return redirect('vehicles')
    return render(request, "vehicles.html", {'vehicle': vehicle})