from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User




Property_Type = [ 
    ('250 SQM Lifecamp 1','250 SQM Lifecamp 1' ),
    ('300 SQM Lifecamp 1','300 SQM Lifecamp 1' ),
    ('500 SQM Lifecamp 1','500 SQM Lifecamp 1' ),
    ('750 SQM Lifecamp 1','500 SQM Lifecamp 1' ),
    ('4 Bedroom FD Lifecamp 1','4 BD fully detached duplex Lifecamp 1' ),
    ('4 Bedroom SD Lifecamp 1','4 BD semi detached duplex Lifecamp 1' ),
    ('3 Bedroom T Lifecamp 1','3 BD Terrace duplex Lifecamp 1' ),
    ('3 Bedroom T Lifecamp 1','3 BD Terrace duplex Lifecamp 1' ),

    ('250 SQM Lifecamp 2','250 SQM Lifecamp 2' ),
    ('300 SQM Lifecamp 2','300 SQM Lifecamp 2' ),
    ('500 SQM Lifecamp 2','500 SQM Lifecamp 2' ),
    ('750 SQM Lifecamp 2','500 SQM Lifecamp 2' ),
    ('4 Bedroom FD Lifecamp 2','4 BD fully detached duplex Lifecamp 2' ),
    ('4 Bedroom SD Lifecamp 2','4 BD semi detached duplex Lifecamp 2' ),
    ('3 Bedroom T Lifecamp 2','3 BD Terrace duplex Lifecamp 2' ),
    ('3 Bedroom T Lifecamp 2','3 BD Terrace duplex Lifecamp 2' ),

    
    ('250 SQM Katampe Extention','250 SQM Lifecamp 2' ),
    ('300 SQM Katampe Extention','300 SQM Lifecamp 2' ),
    ('500 SQM Katampe Extention','500 SQM Lifecamp 2' ),
    ('750 SQM Katampe Extention','500 SQM Lifecamp 2' ),
    ('4 Bedroom FD Katampe Extention','4 BD fully detached duplex Katampe Extention' ),
    ('4 Bedroom SD Katampe Extention','4 BD semi detached duplex Katampe Extention' ),
    ('3 Bedroom T Katampe Extention','3 BD Terrace duplex Katampe Extention' ),
    ('3 Bedroom T Katampe Extention','3 BD Terrace duplex Katampe Extention' ),  


    ('250 SQM Karsana','250 SQM Karsana' ),
    ('300 SQM Karsana','300 SQM Karsana' ),
    ('500 SQM Karsana','500 SQM Karsana' ),
    ('750 SQM Karsana','500 SQM Karsana' ),
    ('4 Bedroom FD Karsana','4 BD fully detached duplex Karsana' ),
    ('4 Bedroom SD Karsana','4 BD semi detached duplex Karsana' ),
    ('3 Bedroom T Karsana','3 BD Terrace duplex Karsana' ),
    ('3 Bedroom T Karsana','3 BD Terrace duplex Karsana' ),   
 
 
                   ]


class Property(models.Model):
    
    building_type= models.CharField(choices=Property_Type,max_length=120, null= False, blank= False)
    initial_quantity= models.IntegerField(null= False, blank= False)
    quantity_in_stock= models.IntegerField( null= False, blank= False) 
    quantity_sold = models.IntegerField( null= False, blank= False) 
    price= models.IntegerField( null= False, blank= False)
    #quantity_in_stock= initial_quantity - quantity_sold 

    def __str__(self):
        return self.building_type
    
    
    


class Agent(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = models.IntegerField()
    email = models.EmailField(max_length=130)
    address = models.CharField(max_length=300)
    number_of_properties_sold= models.IntegerField(null=True, blank=True)
    

    def __str__(self):
        return self.first_name + ' '+ self.last_name
    

class Client(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = models.IntegerField()
    email = models.EmailField(max_length=130)
    building_type= models.ForeignKey(Property, on_delete=models.CASCADE)
    price= models.IntegerField( null= False, blank= False)
    amount_paid= models.IntegerField(null= False, blank= False)
    amount_left= models.IntegerField( null= False, blank= False)
    #amount_left= price-amount_paid
    sales_date= models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=300)
    agent_name = models.ForeignKey(Agent, blank=True, null=True,on_delete= models.SET_NULL)
    agent_comment= models.TextField(max_length=300)
    client_image= models.ImageField(null=True, blank=True, upload_to="images/")
    


    def __str__(self):
        return self.first_name + ' '+ self.last_name
    



    
    
