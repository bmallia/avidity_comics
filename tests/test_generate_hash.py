import pytest
import os
import collections
from core.comicsApp.comics_helper import generate_hash


@pytest.fixture
def parameters_auth():
    public_key = os.environ.get("COMICS_PUBLIC_KEY")
    private_key = os.environ.get("COMICS_PRIVATE_KEY")
    authparameter = collections.namedtuple("Authparameters", "publickey privatekey")
    return authparameter(publickey=public_key, privatekey=private_key) 


def test_generate_hash_ok(parameters_auth):
    
    current_ts, gen_hashed = generate_hash(parameters_auth.privatekey, parameters_auth.publickey)
    
    assert current_ts
    assert gen_hashed
    
def test_generate_hash_no_public_key(parameters_auth):
    with pytest.raises(ValueError):
        current_ts, gen_hashed = generate_hash(parameters_auth.privatekey)

def test_generate_hash_no_private_key(parameters_auth):
    with pytest.raises(ValueError):
        current_ts, gen_hashed = generate_hash(parameters_auth.publickey)