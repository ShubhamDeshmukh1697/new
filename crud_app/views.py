from django.shortcuts import render,redirect
from .models import Product

# Create your views here.
def home(request):
    prods = Product.objects.all()
    if request.method == "POST":
        pname = request.POST.get('name')
        category = request.POST.get('category')
        price= request.POST.get('price')
        obj = Product(pname=pname,category = category,price=price)
        obj.save()
        return redirect('home')
    return render(request, 'home.html',{'prods':prods})


def deleteOrder(request,pk):
    prod = Product.objects.get(pid=pk)
    prod.delete()
    prods = Product.objects.all()
    return redirect('home')

def updateOrder(request,pk):
    product=Product.objects.get(pid=pk)
    if request.method=="POST":
        pname = request.POST.get('name')
        category = request.POST.get('category')
        price= request.POST.get('price')
        
        p = Product.objects.get(pid=pk)
        p.pname = pname
        p.category = category
        p.price = price
        p.save()   
        return redirect('home')
    return render(request,'update.html',{'product':product})
        
    