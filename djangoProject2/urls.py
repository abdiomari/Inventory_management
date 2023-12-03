"""
URL configuration for djangoProject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from djangoProject2 import settings
from inventory_app import views
from inventory_app.views import generate_excel

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),

    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('signup', views.signup, name='signup'),

    # path('sales/', views.sales, name='sales'),
    # path('purchases/', views.purchases, name='purchases'),

    path('addCustomer/', views.add_customers, name='add_customer'),
    path('addSupplier/', views.add_supplier, name='add_supplier'),
    path('Supplier/', views.view_suppliers, name='view_suppliers'),
    path('Customer/', views.view_customers, name='view_customers'),

    path('addProduct/', views.add_product, name='add_product'),
    path('products/', views.view_products, name='view_products'),
    path('product/<int:prod_id>', views.product_details, name='product_details'),
    path('product/delete/<int:prod_id>', views.delete_product, name='delete_product'),
    path('product/update/<int:prod_id>', views.update_products, name='update_products'),

    path('addOrder/', views.add_order, name='add_order'),
    path('Order/', views.view_order, name='view_order'),
    path('Orders/', views.view_orders, name='view_orders'),
    path('addOrderDetails/', views.add_order_details, name='add_order_details'),
    path('OrderDetails/', views.view_order_details, name='view_order_details'),

    path('addTransactions/', views.add_transactions, name='add_transactions'),
    path('Transactions/', views.view_transactions, name='view_transactions'),
    path('Transactions/', views.view_transactions, name='view_transactions'),

    path('generate-excel/', generate_excel, name='generate_excel'),
    path('view-excel/', views.display_excel, name='view_excel'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
