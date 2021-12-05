import os
import collections
import pytest
import requests

from core.comicsApp.comics_helper import generate_hash
from core.comicsApp.authentication import AuthSingleton

@pytest.fixture
def hash_service():
    public_key = os.environ.get("COMICS_PUBLIC_KEY")
    private_key = os.environ.get("COMICS_PRIVATE_KEY")
    ts, hash = generate_hash(private_key, public_key)
    authparameter = collections.namedtuple("Authparameters", "publickey privatekey timestamp hash")
    hash_service = authparameter(publickey=public_key, privatekey=private_key, timestamp=ts, hash=hash) 
    return AuthSingleton(public_key=hash_service.publickey, private_key=hash_service.privatekey, timestamp=hash_service.timestamp, hash=hash_service.hash)

@pytest.mark.skip(reason="testing not authentication")
def test_request_authentication(hash_service):
    
    res = requests.get(f"http://gateway.marvel.com/v1/public/comics?apikey={hash_service.public_key}&ts={hash_service.timestamp}&hash={hash_service.hash}")
    
    assert res.status_code == 200


def test_find_character_request(hash_service):

    res1 = requests.get(f"https://gateway.marvel.com:443/v1/public/characters?name=Thor&apikey={hash_service.public_key}&ts={hash_service.timestamp}&hash={hash_service.hash}")

    ##sometimes its not loading de response msg even with 200 status code
    assert res1.status_code == 200

    data_json =  res1.json()

    assert data_json
    