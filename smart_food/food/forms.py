from django import forms
from .models import Foods
from datetime import datetime

class FoodForm(forms.ModelForm):
  
  class Meta:
    model = Foods
    fields = ["name", "expirydate", "quantity"]
    widgets = {
      'expirydate': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
    }

  def save(self, *args, **kwargs):
    obj = super(FoodForm, self).save(commit=False)
    obj.create_at = datetime.now()
    obj.update_at = datetime.now()
    obj.save()
    return obj
  
class FoodUpdateForm(forms.ModelForm):
  
  class Meta:
    model = Foods
    fields = ["name", "expirydate", "quantity"]
    widgets = {
      'expirydate': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
    }

  def save(self, *args, **kwargs):
    obj = super(FoodUpdateForm, self).save(commit=False)
    obj.update_at = datetime.now()
    obj.save()
    return obj