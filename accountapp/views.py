from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import NewModel


def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('input_text')

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else :
        data_list = NewModel.objects.all()
        return render(request, 'accountsapp/hello_world.html', context={'data_list': data_list})

class AccountCreatView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


