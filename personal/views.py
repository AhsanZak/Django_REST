from django.shortcuts import render

from Account.models import Account

# Create your views here.

def home_screen_view(request):
    context = {}
    context['some_string']  = "There is  the strinf and there is the number"

    return render(request, 'personal/home.html', context)
