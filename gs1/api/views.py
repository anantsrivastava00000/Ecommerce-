from django.shortcuts import render, redirect, HttpResponse
from .models import Product, Items
from django.contrib import messages
# from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required(login_url='/login')
# @login_required(login_url='/accounts/login') #apne aaap yi leta hai


def home(request):
    products=Product.objects.all()
    print(products)
    return render(request, 'api/home.html', {'products':products})

@login_required
def add_to_cart(request, id):
    product=Product.objects.get(id=id)
    if Items.objects.filter(product=product).exists():
        items=Items.objects.get(product=product)
        if items.quantity < 10:
            quantity=items.quantity
            items.quantity=quantity+1
            items.save()
            return redirect('/go-to-cart/')
        else:
            messages.error(request, 'limit 10')
            return redirect('/home/')
        # return HttpResponse('aa')

    else:
        Items.objects.create(product=product)
        return redirect('/go-to-cart/')
        # return HttpResponse('aa')

    # item, created=Items.objects.get_or_create(product=product)
    # if created:
    #     return redirect('/go-to-cart/')
    # else:
    #     quantity = item.quantity
    #     item.quantity=quantity+1
    #     item.save()
    #     return redirect('/go-to-cart/')


# def go_to_cart(request):
#     items=Items.objects.all()
#     price=sum([item.quantity*item.product.price for item in items])
#     print(price)
#     return render(request, 'api/go_to_cart.html', {'items':items, 'price':price})

def go_to_cart(request):
    
    items=Items.objects.all()
 
        
    total_price=sum([item.quantity*item.product.price for item in items])
    print(total_price)
    return render(request, 'api/go_to_cart.html', {'items':items, 'price':total_price})


def search(request):
    print(request.GET)
    name=request.GET.get('query')
    products=Product.objects.filter(name__icontains=name)
    return render(request, 'api/search.html', {'products':products})


def remove_from_cart(request, id):
    item=Items.objects.get(id=id)
    if item.quantity > 1:
        quantity=item.quantity
        item.quantity=quantity-1
        item.save()
        return redirect('/go-to-cart/')
    else:
        item.delete()
        return redirect('/go-to-cart/')
     
    

# def update_cart(request, id):
 
#     item=Items.objects.get(id=id)
#     if item.quantity < 10:
#         quan=item.quantity
#         item.quantity=quan+1
#         item.save()
#         return redirect('/go-to-cart/')
#     else:
#         messages.error(request, 'limit 10')
#         return redirect('/go-to-cart/')

def update_cart(request, id):
 
    item=Items.objects.get(id=id)
    if item.quantity < 10:
        quan, price=item.quantity, item.product.price
        item.quantity=quan+1
        item.product.price=item.product.price+price
        item.save()
        return redirect('/go-to-cart/')
    else:
        messages.error(request, 'limit 10')
        return redirect('/go-to-cart/')

def delete_cart(request, id):
    item=Items.objects.get(id=id)
    item.delete()
    return redirect('/go-to-cart/')



# def register(request):
#     if request.method == 'POST':
#         form=UserRegistrationForm(request.POST)
#         if form.is_valid():
#            user = form.save(commit=False)
#            user.set_password(form.cleaned_data['password1'])
#            user.save()
#            login(request, user)
#            return redirect('tweet_list')
    
#     else:
#         form = UserRegistrationForm()
    
#     return render(request, 'registration/register.html', {'form': form})