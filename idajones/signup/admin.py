from django.contrib import admin
from signup.models import signup
class signupAdmin(admin.ModelAdmin):
    displaylist=("firstname","email","password","comfirm_password")
    
admin.site.register(signup,signupAdmin)


# Register your models here.
