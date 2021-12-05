import pytest
from core.comicsApp.models import Character
import django

@pytest.fixture
def character():
   django.setup()
   return Character.objects.create(name="hulk", description="Hulk's story description", attributionText="Attribution Marvel")
    ##Character.objects.create(name="Capitan America", description="Captan America's story description", attributionText="Attribution Marvel")



   
