
from django.urls import path
from . import views
urlpatterns = [
    path('initial_registration/register/', views.register, name='register'),
    path('register/', views.register, name='register1'),
    path('initial_login/login/', views.login, name='login'),
    path('initial_registration/login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotPassword/',views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/',views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/',views.resetPassword, name='resetPassword'),
    path('selectAccount/',views.select_account, name='selectAccount'),
    path('deleteAccount/',views.Delete_account, name='deleteAccount'),
    path('initial_registration/',views.select_your_registration, name='initialRegistration'),
    path('initial_login/',views.select_your_login, name='initialLogin'),
    path('profile_management/',views.profileManagement, name='profile_management'),
    path('upload_profile_pic/',views.profilePicUpload, name='upload_profile_pic'),
    path('update_personal_info/',views.update_personal_info, name='update_personal_info'),
    path('user_address/',views.manage_user_address, name='manage_user_address'),
    path('wish_list/',views.go_to_Wish_list, name='go_to_wish_list'),
    path('get_product_for_wish_list/',views.Get_product_for_wish_list, name='get_product_for_wish_list'),
    path('add_to_wish_list/<slug:product_slug>/',views.add_to_wish_list, name='add_to_wish_list'),
    path('sales_report/',views.sales_report, name='sales_report'),
    path('tran_report/',views.all_transaction, name='tran_report'),
    path('delete_tran/<int:id>/',views.delete_transaction, name='delete_tran'),
    path('categories/',views.all_category, name='get_categories'),
    path('popular_product/',views.top_selling_product, name='top_product'),
    path('all_order/',views.see_order_request, name='all_orders'),
    path('delete_order/<int:id>/',views.delete_requested_order, name='delete_orders'),
]