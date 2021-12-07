import os
import time
from tqdm import tqdm
import requests

from django.core.management.base import BaseCommand


from core.comicsApp.comics_helper import generate_hash
from core.comicsApp.authentication import AuthSingleton
from core.comicsApp.models import Character
from core.comicsApp.builder import CharacterBuilder, Director

class Command(BaseCommand):
    """
        This class represents the command that populates the commics information from Marvel's website service using the name as argument"
    Args:
        BaseCommand ([type]): [description]
    """
    help = "populate the commics information from Marvel's website service using the name as argument"

    def __init__(self):
        super().__init__()
        public_key = os.environ.get("COMICS_PUBLIC_KEY")
        private_key = os.environ.get("COMICS_PRIVATE_KEY")
        timestamp, hash_auth = generate_hash(public_key=public_key, private_key=private_key)
        AuthSingleton(public_key=public_key, private_key=private_key , timestamp=timestamp, hash=hash_auth)
        

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="The character's name from the marvel comics")

    def handle(self, *args, **kwargs):
        with tqdm(total=100) as pbar:
            hero_name = kwargs['name']
        
            self.stdout.write(f"Finding requests to send to marvel's website using {hero_name} as parameter:")
            res1 = None
            
            character_builder = CharacterBuilder(name=hero_name, progress_bar=pbar)
            d = Director(character_builder)   
            d.construct_character()
            time.sleep(0.1)
            
            pbar.close()

        self.stdout.write(f"Informations about {hero_name} updated sucessfully")