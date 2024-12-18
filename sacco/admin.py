from django.contrib import admin

from sacco.models import Customer, Deposit
from .models import Loan


# Register your models here.
admin.site.site_header = 'Umoja Sacco Administration'
admin.site.site_title = 'Sacco Admin'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'gender', 'dob', 'account_number']
    search_fields = ['first_name', 'last_name', 'email', 'account_number']
    list_filter = ['gender']
    list_per_page = 25

class DepositAdmin(admin.ModelAdmin):
    list_display = ['customer', 'created_at', 'status', 'amount']
    search_fields = ['customer', 'status', 'amount']
    list_per_page = 25
    list_filter = ['status']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Deposit, DepositAdmin)





# python manage.py --help

# python manage.py createsuperuser
# admin@gmail.com
# 123456

# localhost:8000/admin











# python manage.py --help

#  python manage.py  createsuperuser
# admin@gmail.com
# 123456
# password:pW@3456r   user:hrumojasacco@gmail.com


# access amdin tool
#  localhost:8000/admin