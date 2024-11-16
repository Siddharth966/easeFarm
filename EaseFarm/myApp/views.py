from django.shortcuts import render, redirect
from myApp.models import Contact
from django.contrib import messages
from datetime import datetime
from django.views import View
from .forms import CustomerRegistrationForm, ProductForm, CustomerProfileForm
from .models import Customer, Product, Cart, OrderPlaced
from django.db.models import Q
from django.http import JsonResponse
# my new file

from django.shortcuts import get_object_or_404
from django.utils import timezone

from django.shortcuts import redirect, get_object_or_404
from .models import Product, Cart  # Import your models

from django.shortcuts import redirect, get_object_or_404
from .models import Cart, Product
# myApp/views.py

from .forms import CustomerRegistrationForm, ProductForm, CustomerProfileForm
# myApp/views.py

from .forms import CustomerRegistrationForm, ProductForm, CustomerProfileForm, CartForm



def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'address.html', {'add': add, 'active': 'btn-primary'})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        return render(request, 'index.html')
    return render(request, 'contact.html')


def BorrowProduct(request):
    img = Product.objects.all()
    return render(request, 'BorrowProduct.html', {'img': img})


def Become_supplier(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ProductForm()
    return render(request, 'Become_supplier.html', {'form': form})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'signup.html', {'form': form})


def password_reset(request):
    return render(request, 'password_reset.html')


def password_reset_confirm(request):
    return render(request, 'password_reset_confirm.html')


def change_password(request):
    return render(request, 'change_password.html')


def passwordchangedone(request):
    return render(request, 'passwordchangedone.html')


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product_detail.html', {'product': product})


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone_no']
            another_phone_no = form.cleaned_data['another_phone_no']
            aadhar_card_no = form.cleaned_data['aadhar_card_no']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, email=email, phone_no=phone_no, another_phone_no=another_phone_no,
                           aadhar_card_no=aadhar_card_no, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully')
            return render(request, 'profile.html', {'form': form, 'active': 'btn-primary'})


def search(request):
    query = request.GET['query']
    equip = Product.objects.filter(title__icontains=query)
    params = {'equip': equip}
    return render(request, 'search.html', params)



    if request.method == "POST":
        product_id = request.POST.get('product_id')  # Get product ID from form
        quantity = request.POST.get('quantity')      # Get quantity from form
        print(product_id)

        # Validate the product_id to avoid empty or invalid data
        if not product_id or not product_id.isdigit():
            messages.error(request, "Invalid product ID.")
            return redirect('index')  # Handle invalid product_id

        # Ensure the product exists
        product = get_object_or_404(Product, id=product_id)
        user = request.user

        # Check if the product is already in the cart
        cart_item, created = Cart.objects.get_or_create(user=user, product=product)
        if not created:
            # If the product is already in the cart, update the quantity
            cart_item.quantity += int(quantity)
        else:
            cart_item.quantity = int(quantity)
            cart_item.time = timezone.now()  # Set the current time when the item is added

        cart_item.save()

        messages.success(request, "Product added to cart successfully!")
        return redirect('show_cart')  # Redirect to the cart page

    return redirect('index')







# def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        # print(cart)
        amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.rent_price)
                amount += tempamount
            return render(request, 'add_to_cart.html', {'carts': cart, 'amount': amount})
        else:
            return render(request, 'empty_cart.html')

from django.shortcuts import redirect, get_object_or_404
from .models import Product, Cart

# this is add to cart section
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity', 0)
        product = get_object_or_404(Product, id=product_id)
        try:
            quantity = int(quantity)
        except ValueError:
            quantity = 0
        # Assuming Cart model has a method to add products
        cart, created = Cart.objects.get_or_create(user=request.user, product=product)
           
        if not created:
            # If the product is already in the cart, update the quantity only by the amount specified
            cart.quantity += quantity
        else:
            # If it's a new item in the cart, set the quantity to the form's value
            cart.quantity = quantity
        
        # Save the cart item
        cart.save()

        return redirect('show_cart')  # Redirect to cart page
from django.shortcuts import render
from .models import Cart

def cart_view(request):
    carts = Cart.objects.filter(user=request.user)
    
    # Calculate the total amount for the cart
    total_amount = sum(item.quantity * item.product.rent_price for item in carts)
    
    return render(request, 'add_to_cart.html', {'carts': carts, 'total_amount': total_amount})

     
    



# def show_cart(request):
    from django.shortcuts import render
from .models import Cart  # Assuming Cart is the model for the cart

def show_cart(request):
    
    cart = Cart.objects.filter(user=request.user)

    # Calculate the subtotal for each item and the grand total
    grand_total = 0
    for item in cart:
        item.subtotal = item.quantity * item.product.rent_price  # Subtotal for each item
        grand_total += item.subtotal  # Summing up subtotals for grand total

    return render(request, 'buy_now.html', {'cart': cart, 'grand_total': grand_total})


def remove_from_cart(request, product_id):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, product__id=product_id, user=request.user)
        cart.delete()
        messages.success(request, 'Item removed from cart successfully.')
    else:
        messages.error(request, 'You need to log in to remove items from the cart.')
    return redirect('show_cart')  # Redirect back to the cart view

def update_cart(request, product_id):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, product__id=product_id, user=request.user)
        quantity = int(request.POST.get('quantity', 1))
        cart.quantity = quantity
        cart.save()  # Save the updated quantity

        # Recalculate the total amount for the cart
        total_amount = sum(item.quantity * item.product.rent_price for item in Cart.objects.filter(user=request.user))
        
        return redirect('show_cart')  # Redirect back to the cart page after update
 
def plus_cart(request):
    if request.method == 'GET' and request.user.is_authenticated:
        prod_id = request.GET['prod_id']
        user = request.user
        cart = Cart.objects.get(Q(product=prod_id) & Q(user=user))

        # Increment quantity
        cart.quantity += 1
        cart.save()

        # Recalculate the total amount for the cart
        total_amount = sum(item.quantity * item.product.rent_price for item in Cart.objects.filter(user=user))
        request.session['total_amount'] = total_amount  # Update the session

        data = {
            'quantity': cart.quantity,
            'amount': cart.quantity * cart.product.rent_price,
            'total_amount': total_amount
        }
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    
    
    
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = CustomerRegistrationForm()
    return render(request, 'signup.html', {'form': form})       
        
        


def static_Product_Detail(request):
    return render(request, 'staticProductDetail.html')


def static_Product_Detail1(request):
    return render(request, 'staticProductDetail1.html')



def thank_you(request):
    # Retrieve grand_total from the session
    grand_total = request.session.get('grand_total', 0)
    
    # If grand_total is 0, recalculate it just in case
    if grand_total == 0:
        cart_items = Cart.objects.filter(user=request.user)
        grand_total = sum(item.quantity * item.product.rent_price for item in cart_items)
        request.session['grand_total'] = grand_total  # Store in session for consistency
    
    return render(request, 'thank_you.html', {'grand_total': grand_total})

def confirm_purchase(request):
    # Calculate grand_total from the user's cart items
    cart_items = Cart.objects.filter(user=request.user)
    grand_total = sum(item.quantity * item.product.rent_price for item in cart_items)
    
    # Store grand_total in the session for future reference
    request.session['grand_total'] = grand_total
    
    # Clear the cart after confirming the purchase (optional)
    cart_items.delete()  # This will remove all cart items for the user
    
    # Redirect to thank you page after confirmation
    return redirect('thank_you')


# ................................................................


 
