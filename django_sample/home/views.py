from django.shortcuts import render
from django . http import HttpResponse

from .forms import BookingForm

from .models import Departments,Doctors

# person={
#     'name':'paaachu',
#     'age': 30
    
# }

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def doctors(request):
    dict_doc={
        'doc': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doc)

def booking(request):
     #to save in db
     if request.method =="POST":
         form = BookingForm(request.POST)
         if form.is_valid():
             form.save()
             return render(request,'confirmation.html')

     #to get data from db to ui
     form = BookingForm()
     dict_form = {
         'form': form
         
     }
     return render(request,'booking.html',dict_form)

def contact(request):
    return render(request,'contact.html')
def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)



