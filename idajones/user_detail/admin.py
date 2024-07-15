from django.contrib import admin
from user_detail.models import user_detail

class userdetailAdmin(admin.ModelAdmin):
    list_display=('First_name', 'room_address', 'village_address', 'city_address' ,'pincode_address', 'phone' ,'alt_phone')
    
admin.site.register(user_detail,userdetailAdmin)#it is imp to display
    
