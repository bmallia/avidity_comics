

class Basis:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

class AuthSingleton(Basis):
    """
        This class keeps the need information to authentication in commics marvel services.

        The attributes that you have to pass is:
        public_key
        private_key
        timestamp
        hash
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


       
    def get_timestamp(self):
        """  get the timestamp used to generate the hash

        Returns:
            [timestamp or None]: [a timestamp value]
        """

        if "timestamp" in self._shared_state:
            return self._shared_state["timestamp"]

        return None

    def get_publickey(self):
        """
            get the public key used to generate the hash code

        Returns:
            [str]: [public key]
        """
        if "public_key" in self._shared_state:
            return self._shared_state["public_key"]
        
        return None
            

    def get_hash(self):
        """
        return the hash generated used to authentication on Marvel's api

        Returns:
            [str]: [a hash value]
        """
        if "hash" in self._shared_state:
                return self._shared_state["hash"]

        return None

    def __str__(self):
        return str(self._shared_state)
