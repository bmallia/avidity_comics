from django.shortcuts import render
from core.comicsApp.models import Character
import json

def list_heros(request):
    characters = Character.objects.all()
    
    print(type(characters))
    context = {
        'characters': characters,
    }

    
    

    return render(request, 'commics-info.html', context)
