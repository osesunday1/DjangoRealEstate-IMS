import django_filters
from django import forms
from django.forms import ModelForm
from .models import *



class DateInput(forms.DateInput):
    input_type='date'



class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields= ('first_name', 'building_type', 'agent_name',)
        labels= {
            'first_name': 'Hahaha',
            'building_type': '',
            'agent_name': '',
        }

        widgets= {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
            'building_type': forms.Select(attrs={'class':'form-select', 'placeholder': 'Property'}),
            'agent_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Agent'}),
        }

