from django.urls import path
from . import views



app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='create'),
    path('<int:order_id>/', views.detail, name='detail'),
    path('apply/<int:order_id>/', views.coupon_apply, name='coupon_apply'),
    path('all_order/', views.show_orders, name='show_orders'),
    path('detail_order/<int:order_id>', views.show_detail_order, name='show_detail_order'),
]