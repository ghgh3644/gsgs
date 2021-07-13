from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import NewModel


def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('input_text')

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()


        return render(request, 'accountsapp/hello_world.html', context={'model_instance': model_instance})
    else :
        return render(request, 'accountsapp/hello_world.html', context={'text': 'GET METHOD!'})
