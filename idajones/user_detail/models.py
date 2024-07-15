from django.db import models

class user_detail(models.Model):
    First_name=models.CharField(max_length=50)
    First_name=models.CharField(max_length=50)
    room_address=models.IntegerField()
    village_address=models.CharField( max_length=50)
    city_address=models.CharField( max_length=50)
    state_address=models.CharField( max_length=50)
    pincode_address=models.IntegerField()
    phone=models.IntegerField()
    alt_phone=models.IntegerField()
    

    
   