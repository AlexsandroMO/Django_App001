
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
#from .models import MinhasConta
#from .forms import MinhasContatForm
from django.contrib import messages



def Homes(request):
    return HttpResponse("<h1>Hello, let's get start!</h1>")




#def Cotation(request):
    #return render(request, 'coin/site-cotation.html',{'bitcoin': bitcoin,'all_cotation': all_cotation})
