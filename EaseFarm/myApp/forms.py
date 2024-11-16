from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer, Product
from django.db import models
from .models import Product
from .models import Cart as CartModel





class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Password'}))
    password2 = forms.CharField(label='confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Confirm Password'}))
    email = forms.CharField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Username'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Enter your Username'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Enter your Password'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'), strip=False, widget= forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget= forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation. password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('New Password'), strip=False, widget= forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-passowrd', 'class':'form-control'}), help_text=password_validation. password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-passowrd', 'class':'form-control'}))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name_of_owner', 'house_no', 'district', 'city', 'zipcode',
                  'state', 'phone_no', 'another_phone_no', 'title',
                  'rent_price', 'brand', 'description', 'product_image']


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_no', 'another_phone_no', 'aadhar_card_no', 'locality', 'city', 'state', 'zipcode']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
                   'another_phone_no': forms.TextInput(attrs={'class': 'form-control'}),
                   'aadhar_card_no': forms.TextInput(attrs={'class':'form-control'}),
                   'locality': forms.TextInput(attrs={'class': 'form-control'}),
                   'city': forms.TextInput(attrs={'class': 'form-control'}),
                   'state': forms.Select(attrs={'class': 'form-control'}),
                   'zipcode': forms.NumberInput(attrs={'class': 'form-control'})}
        



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    name = models.CharField(max_length=100)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


    @property
    def total_price(self):
        return self.quantity * self.product.rent_price if self.product.rent_price else 0



class CartForm(forms.ModelForm):
    class Meta:
        model = CartModel  # Using the renamed model
        fields = '__all__'  # Adjust this as needed

        



                    