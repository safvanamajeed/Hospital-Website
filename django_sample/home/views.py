from django.shortcuts import render
from django . http import HttpResponse

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
    return render(request,'doctors.html')
def booking(request):
     return render(request,'booking.html')

def contact(request):
    return render(request,'contact.html')
def department(request):
    return render(request,'department.html')



