from django.urls import path

from .import views

urlpatterns = [
    path('place_order/',views.place_order, name='place_order'),
    path('order_complete/',views.order_complete, name='order_complete'),
    path('success/', views.success_view, name='success_view'),
    #path('invoice/',views.invoice, name='invoice'),
    path('order_history/',views.order_history, name='order-history'),
    path('recent_order/',views.recent_order, name='recent-order'),
    path('delete_orders/<int:id>/',views.order_delete, name='order_delete'),
    
    
]