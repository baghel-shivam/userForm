import imp
from urllib import request
from django.shortcuts import render , redirect
from .models import User

# Create your views here.
def index(request):
    return render(request,"index.html")

def saveData(request):
   pin = request.POST['pin']
   house = request.POST['house']
   apartment = request.POST['apartment']
   area = request.POST['area']
   landmark = request.POST['landmark']
   visit = request.POST['visit']
   data = User(pin=pin, house = house, apartment = apartment, area=area,landmark =landmark, visit = visit)
   data.save()
   return redirect(index)
