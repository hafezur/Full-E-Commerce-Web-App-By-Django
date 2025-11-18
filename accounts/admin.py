from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # akhane ModelAdmin thakto by default but jahato ModelAdmin k override kora hoyasa tai UserAdmin use kora hoyasa. 
from .models import Account,WishListProduct

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email',) # ai email a click korla user ar sob data dakte parbo..
    readonly_fields = ('last_login', 'date_joined') # ai field edit kora jabe na.
    ordering = ('-date_joined',) # 
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(WishListProduct)



