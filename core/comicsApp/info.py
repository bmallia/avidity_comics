

class Basis:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

class AuthSingleton(Basis):
    """
        This class keeps the need information to authentication in commics marvel services.
    """
    def __init__(self, **kwargs):
        Basis.__init__(self)
        self._shared_state.update(kwargs)

        if not "timestamp" in self._shared_state:
            raise AttributeError("ts attribute doesn't exist")

        if not "hash" in self._shared_state:
            raise AttributeError("hash attribute doesn't exist")

        if not "public_key" in self._shared_state:
            raise AttributeError("public key attribute doesn't exist")

        if not "private_key" in self._shared_state:
            raise AttributeError("private key attribute doesn't exist")
       

    def __str__(self):
        return str(self._shared_state)
