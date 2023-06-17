from django.shortcuts import render
from App.models import Product
from django.http import HttpResponseRedirect
from django.contrib import messages

#View the product individually

def index(request):
    context = {}
    return render(request, 'index.html', context)


# ====================== VIEWS PARA VERSION CON MODAL 100% =========================

def home(request):
    all_product=Product.objects.all().order_by('-created')
    return render(request,'home.html', {'products':all_product})

#Add product
def add_product(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('purchase') and request.POST.get('sale') and request.POST.get('qty') and request.POST.get('gender') or request.POST.get('note'):
            product=Product()
            product.name=request.POST.get('name')
            product.purchase=request.POST.get('purchase')
            product.sale=request.POST.get('sale')
            product.qty=request.POST.get('qty')
            product.gender=request.POST.get('gender')
            product.note=request.POST.get('note')
            product.save()
            messages.success(request," 👍 Product added successfully! ")
            return HttpResponseRedirect('/home')
    else:
        return render(request, 'add.html')


#View the product individually
def product(request, product_id):
    product=Product.objects.get(id=product_id)
    if product != None:
        return render(request, 'edit.html', {'product':product})
    

#Edit product
def edit_product(request):
    if request.method == 'POST':
        product=Product.objects.get(id = request.POST.get('id'))
        if product != None:
            product.name=request.POST.get('name')
            product.purchase=request.POST.get('purchase')
            product.sale=request.POST.get('sale')
            product.qty=request.POST.get('qty')
            product.gender=request.POST.get('gender')
            product.note=request.POST.get('note')
            product.save()
            messages.success(request," 👍 Product updated successfully! ")
            return HttpResponseRedirect('/home')
    

#Delete product
def delete_product(request, product_id):
    product=Product.objects.get(id = product_id)
    product.delete()
    messages.success(request," 👍 Product deleted successfully! ")
    return HttpResponseRedirect('/home')


# ====================== VIEWS PARA VERSION CON MODAL 100% =========================

def home2(request):
    all_product=Product.objects.all().order_by('-created')
    return render(request,'home2.html', {'products':all_product})

#Add product
def add2_product(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('purchase') and request.POST.get('sale') and request.POST.get('qty') and request.POST.get('gender') or request.POST.get('note'):
            product=Product()
            product.name=request.POST.get('name')
            product.purchase=request.POST.get('purchase')
            product.sale=request.POST.get('sale')
            product.qty=request.POST.get('qty')
            product.gender=request.POST.get('gender')
            product.note=request.POST.get('note')
            product.save()
            messages.success(request," 👍 Product added successfully! ")
            return HttpResponseRedirect('/home2')
    else:
        return render(request, 'add2.html')


#View the product individually
def product2(request, product_id):
    product=Product.objects.get(id=product_id)
    if product != None:
        return render(request, 'edit2.html', {'product':product})
    

#Edit product
def edit2_product(request):
    if request.method == 'POST':
        product=Product.objects.get(id = request.POST.get('id'))
        if product != None:
            product.name=request.POST.get('name')
            product.purchase=request.POST.get('purchase')
            product.sale=request.POST.get('sale')
            product.qty=request.POST.get('qty')
            product.gender=request.POST.get('gender')
            product.note=request.POST.get('note')
            product.save()
            messages.success(request," 👍 Product updated successfully! ")
            return HttpResponseRedirect('/home2')
    

#Delete product
def delete2_product(request, product_id):
    product=Product.objects.get(id = product_id)
    product.delete()
    messages.success(request," 👍 Product deleted successfully! ")
    return HttpResponseRedirect('/home2')
