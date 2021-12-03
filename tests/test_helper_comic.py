import os
import collections
import pytest

from core.comicsApp.info import AuthSingleton
from core.comicsApp.comics_helper import generate_hash

@pytest.fixture
def hash_service():
    public_key = os.environ.get("COMICS_PUBLIC_KEY")
    private_key = os.environ.get("COMICS_PRIVATE_KEY")
    ts, hash = generate_hash(private_key, public_key)
    authparameter = collections.namedtuple("Authparameters", "publickey privatekey timestamp hash")
    return authparameter(publickey=public_key, privatekey=private_key, timestamp=ts, hash=hash) 

def test_singleton_ok(hash_service):
    auth = AuthSingleton(public_key=hash_service.publickey, private_key=hash_service.privatekey, timestamp=hash_service.timestamp, hash=hash_service.hash)
    assert auth

def test_singleton_no_ts_parameter():
   with pytest.raises(AttributeError):
        auth = AuthSingleton(public_key=hash_service.publickey, private_key=hash_service.privatekey, hash=hash_service.hash)
        assert auth

def test_singleton_no_hash_parameter():
    with pytest.raises(AttributeError):
        auth = AuthSingleton(public_key=hash_service.publickey, private_key=hash_service.privatekey, timestamp=hash_service.timestamp)
        assert auth

def test_singletion_no_publickey_parameter():
    with pytest.raises(AttributeError):
        auth = AuthSingleton(private_key=hash_service.privatekey, timestamp=hash_service.timestamp, hash=hash_service.hash)
        assert auth    



