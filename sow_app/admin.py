from django.contrib import admin

from .models import Client
from .models import Property
from .models import Agent


#admin.site.register(Client)
#admin.site.register(Property)
#admin.site.register(Agent)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone','email','building_type','sales_date','agent_name')
    ordering= ('first_name',)
    search_fields=('first_name','last_name')
    list_filter=('sales_date','building_type','agent_name','first_name')



@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone','email','address','number_of_properties_sold')
    ordering= ('first_name',)
    search_fields=('first_name','last_name')
    list_filter=('number_of_properties_sold',)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('building_type','initial_quantity','quantity_in_stock','quantity_sold')
    ordering= ('building_type',)
    search_fields=('building_type',)
    list_filter=('building_type',)