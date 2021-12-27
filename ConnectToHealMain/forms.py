from django import forms
from django.db.models import fields
# from django.forms import ModelForm, widgets
from django.contrib.admin.widgets import AdminTimeWidget
from django.forms import widgets
from .models import *

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = DiscussionModel
        fields = ['info']

class DateInput(forms.DateInput):
    input_type = 'date'
    
class BookAppointmentForm(forms.ModelForm):
    fromTime = forms.TimeField(widget=AdminTimeWidget())
    toTime = forms.TimeField(widget=AdminTimeWidget())
    class Meta:
        model = BookAppointmentModel
        widgets = {
            'date': DateInput()
        }
        fields = ['date','fromTime','toTime']
        
        