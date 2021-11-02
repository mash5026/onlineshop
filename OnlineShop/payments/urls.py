from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('go-to-gateway/<int:order_id>/<price>/', views.go_to_gateway_view, name='go_to_gateway_view'),
    path('callback-gateway/', views.callback_gateway_view, name='callback_gateway_view'),
]