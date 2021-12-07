import pytest
import os
import collections
import requests

from core.comicsApp.builder import Director, CharacterBuilder
from core.comicsApp.comics_helper import generate_hash
from core.comicsApp.authentication import AuthSingleton
from core.comicsApp.management.commands.populatecomics import Command
from core.comicsApp.models import Character

@pytest.fixture
def hash_service():
    print("\n Test Generating info  to get data from marvel's api")
    public_key = os.environ.get("COMICS_PUBLIC_KEY")
    private_key = os.environ.get("COMICS_PRIVATE_KEY")
    ts, hash = generate_hash(private_key, public_key)
    authparameter = collections.namedtuple("Authparameters", "publickey privatekey timestamp hash")
    hash_service = authparameter(publickey=public_key, privatekey=private_key, timestamp=ts, hash=hash) 
    return AuthSingleton(public_key=hash_service.publickey, private_key=hash_service.privatekey, timestamp=hash_service.timestamp, hash=hash_service.hash)

@pytest.mark.django_db
def test_builder_ok(db):
    stdout = Command().stdout
    char = Character.objects.get(pk=2)
    assert char.name == "Thor"
    
    ##character_builder = CharacterBuilder("Thor" , stdout)
    ##d = Director(character_builder)
    ##d.construct_character()
    assert 1 == 1
    

def test_simple(db):
    assert 1 == 1 