from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from .views import add_to_cart, cart_view
from .views import remove_from_cart

# from myApp.views import add_to_cart, BorrowProductView, own_product_view, borrow_product_view

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('address/', views.address, name='address'),
    path('BorrowProduct/', views.BorrowProduct, name='BorrowProduct'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show_cart'),
    path('pluscart/', views.plus_cart, name='plus_cart'),
    path('show_cart/', views.show_cart, name='show_cart'),
    #path('minuscart/', views.minus_cart, name='minus_cart'),
    
    
    path('product_detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('static-Product-Detail/', views.static_Product_Detail, name='static-Product-Detail'),
    path('static-Product-Detail1/', views.static_Product_Detail1, name='static-Product-Detail1'),
    
    
    path("signup/", views.CustomerRegistrationView.as_view(), name="signup"),
   
    path("login/", auth_views.LoginView.as_view(template_name= 'login.html', authentication_form = LoginForm), name='login'),
    
     path("login1/", auth_views.LoginView.as_view(template_name= 'login1.html', authentication_form = LoginForm), name='login1'),
     
    path("logout/", auth_views.LogoutView.as_view(next_page = 'login'), name='logout'),
    path("Become_supplier/", views.Become_supplier, name="Become_supplier"),
    path("password_reset/", views.password_reset, name='password_reset'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("change_password/", auth_views.PasswordChangeView.as_view(template_name='change_password.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='change_password'),
    
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html", form_class=MyPasswordResetForm), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html", form_class=MySetPasswordForm), name="password_reset_confirm"),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete"),

    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    
    
    
    # new addition
    path('BorrowProduct/', views.BorrowProduct, name='BorrowProduct'),
   
      path('admin/', admin.site.urls),


path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove-from-cart'),

    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('cart/', cart_view, name='cart'),
     path('update-cart/<int:product_id>/', views.update_cart, name='update-cart'),
     path('plus_cart/', views.plus_cart, name='plus_cart'),

 path('thank-you/', views.thank_you, name='thank_you'),
 path('confirm-purchase/', views.confirm_purchase, name='confirm-purchase'),
    
]
