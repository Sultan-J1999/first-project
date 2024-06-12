from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from app.models import data

from app.Forms import MemberForms


def first(request):
   
   template = loader.get_template('first.html')
   
   return HttpResponse(template.render())



def all_expenses(request):
  mydata = data.objects.all()
  template = loader.get_template('all_expenses.html')
  context = {
    'mydata': mydata,
  }
  return HttpResponse(template.render(context,request))


def input_expneses(request):
  if request.method=="POST":
    form = MemberForms(request.POST)
    if form.is_valid():
      date = form.cleaned_data['date']
      salary = form.cleaned_data['salary']
      Location = form.cleaned_data['Location']
      description = form.cleaned_data['description']
      new_member = data(date=date , salary=salary,Location=Location,description=description)
      new_member.save()
      return HttpResponseRedirect("/input_expneses")
  else: 
      form =MemberForms()
      template=loader.get_template('input_expenses.html')
      context ={
      'form': form

      }
      return HttpResponse(template.render(context,request))