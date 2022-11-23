"""rishattest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_default),
    path('buy/<int:id>/', views.get_stripe_id),
    path('buy/order/<int:id>/', views.buy_order_page),
    path('item/<int:id>/', views.first_page),
    path('create-checkout-session/', views.buy_item_page),
    path('success/', views.success_page, name = 'success'),
    path('cancel/', views.cancel_page, name = 'cancel'),
]

