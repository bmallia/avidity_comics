from django.shortcuts import render
from core.comicsApp.models import Character
import json

def list_heros(request):
    characters = Character.objects.all()
    
    context = {
        'data': characters,
    }

    return render(request, 'commics-info.html', context)
