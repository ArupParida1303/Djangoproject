from django.shortcuts import render,redirect

# Create your views here.

from app8.models import Product_Model

# Create your views here.
def show(request):
    return render(request,"index.html",{"photos":Product_Model.objects.all()})


def save_photo(request):
    id = request.POST.get("iid")
    name = request.POST.get("iname")
    price = request.POST.get("iprice")
    photo = request.FILES['iphoto']
    Product_Model(pno=id, pname=name,pprice=price,pphoto=photo).save()
    return redirect('index')


def delete(request):
    delnum = request.POST["idno"]
    Product_Model.objects.filter(pno=delnum).delete()
    return show(request)
