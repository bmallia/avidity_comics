import hashlib
import datetime


def generate_hash(private_key= None, public_key=None):
    """
        Generate the hash thats is necessary to authentication in comics marvel service

    Args:
        private_key ([type]):  
            private key generated in comics marvel's website. See the documentation http://developer.marvel.com/docs]]
            public_key ([type]): [public key genereted in comics marcel's website. See the documentation http://developer.marvel.com/docs]]

    Returns:
        [tuple]: [the timstamp generated with the hash and the hash]
    """

    if not private_key:
        raise ValueError("parameter private key is necessary to generate hash")

    if not public_key:
        raise ValueError("parameter public key is necessary to generate hash")

    current_ts = datetime.datetime.now().timestamp()
    parameters = f"{current_ts}{private_key}{public_key}".encode('utf-8')
    result = hashlib.md5(parameters)
    return current_ts, result.hexdigest()
