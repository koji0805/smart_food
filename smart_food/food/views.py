from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import(
  View, TemplateView, RedirectView
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
  CreateView, UpdateView, DeleteView,
  FormView,
)
from . import forms
from datetime import datetime
from .models import Foods
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class IndexView(View):
  
  def get(self, request, *args, **kwargs):
    food_form = forms.FoodForm()
    return render(request, "index.html", context={
      "food_form":food_form,
    })
    
  def post(self, request, *args, **kwargs):
    food_form = forms.FoodForm(request.POST or None)
    if food_form.is_valid():
      food_form.save()
    return render(request, "index.html", context={
      "food_form": food_form,
    })
    
class HomeView(TemplateView):
  
  template_name = "home.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    print(kwargs)
    context["name"] = kwargs.get("name")
    context["time"] = datetime.now()
    return context
  
  
class FoodDetailView(DetailView):
  model = Foods
  template_name = "food.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    print(context)
    # context["form"] = forms.FoodForm()
    return context
  
  
class FoodListView(ListView):
  model = Foods
  template_name = "food_list.html"
  
  def get_queryset(self):
    qs = super(FoodListView, self).get_queryset()
    if "name" in self.kwargs:
      qs = qs.filter(name__startswith=self.kwargs["name"])
    qs = qs.order_by("expirydate")
    return qs
  
class FoodCreateView(CreateView):
  model = Foods
  form_class = forms.FoodForm
  template_name = "add_food.html"
  success_url = reverse_lazy("food:list_foods")
  
  def form_valid(self, form):
    form.instance.create_at = datetime.now()
    form.instance.update_at = datetime.now()
    return super(FoodCreateView, self).form_valid(form)
  
  def get_initial(self, **kwargs):
    initial = super(FoodCreateView, self).get_initial(**kwargs)
    initial["name"] = "sample"
    return initial
  
class FoodUpdateView(SuccessMessageMixin, UpdateView):
  
  template_name = "update_food.html"
  model = Foods
  form_class = forms.FoodUpdateForm
  success_message = "更新に成功しました"

  def get_success_url(self):
    return reverse_lazy("food:edit_food", kwargs={"pk": self.object.id})
  
  def get_success_message(self, cleaned_data):
    print(cleaned_data)
    return cleaned_data.get("name") + "を更新しました"
  
class FoodDeleteView(DeleteView):
  model = Foods
  template_name = "delete_food.html"
  success_url = reverse_lazy("food:list_foods")
  
  
class FoodFormView(FormView):
  
  template_name = "form_food.html"
  form_class = forms.FoodForm
  success_url = reverse_lazy("food:list_foods")
  
  def get_initial(self):
    initial = super(FoodFormView, self).get_initial()
    initial["name"] = "form sample"
    return initial
  
  def form_valid(self, form):
    if form.is_valid():
      form.save()
    return super(FoodFormView, self).form_valid(form)
  

class FoodRedirectView(RedirectView):
  url = "https://google.co.jp"
  
  def get_redirect_url(self, *args, **kwargs):
    food = Foods.objects.first()
    if "pk" in kwargs:
      return reverse_lazy("food:detail_food", kwargs={"pk": kwargs["pk"]})
    
    return reverse_lazy("food:edit_food", kwargs={"pk": food.pk})