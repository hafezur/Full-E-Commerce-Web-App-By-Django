from django.urls import path
from . import views
urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('order_request/', views.Order_request, name='order_request'),
    path('order_cancel/<int:id>/', views.Cancel_order, name='order_cancel'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.comment_and_review, name='comment_and_review'),
]