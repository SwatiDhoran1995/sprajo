from re import template

from django.shortcuts import render, HttpResponseRedirect
from .forms import ProductInfo
from .models import Sprajo
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request,'SERVICES.html')
@csrf_protect
def add_show(request):
    if request.method == 'POST':
        pi = ProductInfo(request.POST)
        if pi.is_valid():
            name=pi.cleaned_data['Name']
            img = pi.cleaned_data['Image']
            dec = pi.cleaned_data['description']
            cap = pi.cleaned_data['capacity']
            uni = pi.cleaned_data['unit']
            pri = pi.cleaned_data['price']
            product= Sprajo(Name=name,Image=img,description=dec,capacity=cap,unit=uni,price=pri)
            product.save()
            pi= ProductInfo()
            return render(request, 'AddandShow.html', {'form': pi})
    else:
        pi = ProductInfo()
    item = Sprajo.objects.all()
    return render(request, 'AddandShow.html', {'form': pi,'itm':item})

def displayproduct(request):
    return render(request,'product.html',)

def delete_data(request,id):
    if request.method == 'POST' :
        dele= Sprajo.objects.get(pk=id)
        dele.delete()
        return HttpResponseRedirect('displayproduct/')

def update_data(request,id):
    if request.method == 'POST':
        update =Sprajo.objects.get(pk=id)
        pi=ProductInfo(request.POST,instance=update)
        if pi.is_valid():
            pi.save()
        else:
            update=Sprajo.objects.get(pk=id)
            pi=ProductInfo(instance=update)
    return render(request,'updateproduct.html',{'form':pi})






