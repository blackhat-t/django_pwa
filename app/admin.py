from django.contrib import admin
from .models import Mpesa

class  MpesaAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'amount','created_on' )
    list_filter = ('phone_number', )
    search_friends = ['phone_number','amount']

admin.site.register(Mpesa, MpesaAdmin)