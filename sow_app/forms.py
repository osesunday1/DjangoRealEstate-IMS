from django import forms
from django.forms import ModelForm
from .models import *




class DateInput(forms.DateInput):
    input_type='date'




#create a client form
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields= ('first_name', 'last_name','phone','email',
                 'building_type', 'price', 'amount_paid','amount_left',
                 'sales_date','address','agent_name','agent_comment', 'client_image')
        
        widgets= {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'building_type': forms.Select(attrs={'class':'form-select', 'placeholder': 'Type of Property'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'amount_paid': forms.NumberInput(attrs={'class':'form-control'}),
            'amount_left': forms.NumberInput(attrs={'class':'form-control'}),
            'sales_date':DateInput (attrs={'class':'form-control', 'placeholder': 'Date'}),
            #'sales_date': forms.SelectDateWidget(attrs={'class':'form-control', 'placeholder': 'Amount Paid'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'agent_name':forms.Select(attrs={'class':'form-select'}),
            'agent_comment':forms.Textarea(attrs={'class':'form-control'}),

        }

'''
        labels= {
            'name': '',
        }

'''
        

#create a property form
class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields= ('building_type', 'initial_quantity','quantity_in_stock','quantity_sold','price')
        
        widgets= {
            'building_type': forms.Select(attrs={'class':'form-select', 'placeholder': 'Type of Property'}),
            'initial_quantity': forms.NumberInput(attrs={'class':'form-control'}),
            'quantity_in_stock': forms.NumberInput(attrs={'class':'form-control'}),
            'quantity_sold':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
        }

'''
        labels= {
            'name': '',
        }

'''
    

#create a Agent form
class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields= ('first_name', 'last_name','phone','email','address','number_of_properties_sold',)
        
        widgets= {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'number_of_properties_sold': forms.NumberInput(attrs={'class':'form-control'}),

        }

'''
        labels= {
            'name': '',
        }

'''
        