from django.shortcuts import render, redirect
from .forms import AssistanceForm
from .models import Assistance, AssistanceType
from django.contrib import messages


def request_assistance(request):
    if request.method == 'POST':
        assistance_form = AssistanceForm(request.POST)
        if assistance_form.is_valid():
            data = assistance_form.cleaned_data
            victim_number = data['victim_number']
            assistance_type = AssistanceType.objects.filter(name=data['assistance_type'])[0]
            remark = data['remark']
            assistance = Assistance(victim_number=victim_number, remark=remark)
            assistance.assistance_type = assistance_type
            assistance.user = request.user
            assistance.save()
            messages.success(request, "request has been sent successfully")
            
        return redirect('/assistance/create')
    if request.method == 'GET':
        assistance_form = AssistanceForm()
        return render(request, 'assistance_app/request.html', {'assistance_form': assistance_form})
      
      
def add(request):
    return render(request, 'assistance_app/add.html')

