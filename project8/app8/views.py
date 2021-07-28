from django.shortcuts import render,redirect

# Create your views here.

from app8.models import Product_Model

# Create your views here.
def show(request):
    return render(request,"index.html",{"photos":Product_Model.objects.all()})


def save_photo(request):
    id = request.POST.get("pno")
    name = request.POST.get("name")
    price = request.POST.get("price")
    photo = request.FILES['photo']
    Product_Model(pno=id, name=name,price=price,photo=photo).save()
    return redirect('main')


def delete(request):
    delnum = request.POST["idno"]
    Product_Model.objects.filter(pno=delnum).delete()
    return show(request)
