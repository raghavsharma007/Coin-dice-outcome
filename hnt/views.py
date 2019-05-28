from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import random

def index(request):
    return render(request,'base.html')
def calculate(request):
    coin = request.POST.get('coin','off')
    dice = request.POST.get('dice','off')

    if coin == 'on':
        x = np.random.randint(0,2)
        if x == 0:
            output='Head!!'
            return render(request, 'calculate.html', {'output': output})
        else:
            output='Tail!!'
            return render(request, 'calculate.html', {'output':output})
    if dice == 'on':
        output = np.random.randint(1,7)
        return render(request, 'calculate.html', {'output':output})
    else:
        return HttpResponse('<h1>Please select one and try again!!</h1>')
