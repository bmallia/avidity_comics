import os
import time
from tqdm import tqdm
import requests

from django.core.management.base import BaseCommand


from core.comicsApp.comics_helper import generate_hash
from core.comicsApp.authentication import AuthSingleton
from core.comicsApp.models import Character

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
        hero_name = kwargs['name']

        self.stdout.write(f"Finding requests to send to marvel's website:")

        with tqdm(total=100) as pbar:
            res1 = None

            try:
                res1 = requests.get(f"https://gateway.marvel.com:443/v1/public/characters?name={hero_name}&apikey={AuthSingleton().public_key}&ts={AuthSingleton().timestamp}&hash={AuthSingleton().hash}")
            except requests.exceptions.ConnectionError as e:
                self.stdout.write("Connection erro while getting the character's mavel information")
                exit(1)
            
            data_json =  res1.json()
            pbar.update(100)
            if data_json:
                results = data_json['data']['results']
                for result in results:
                    char_filterd = Character.objects.filter(name=hero_name)
                    if char_filterd.exists():
                        char_filterd.update(description=result['description'], attributionText=data_json['attributionText'], stories=result['stories']['items'])
                        self.stdout.write(f"Character updated!")
                    else:
                        character = Character(name=result["name"], description=result['description'], attributionText=data_json['attributionText'], stories=result['stories']['items'])
                        character.save()     
                        self.stdout.write(f"Character saved")
                        
                    time.sleep(0.1)
                    pbar.update(int(100 / len(results)))
                    
            pbar.update(100)
            pbar.close()

        self.stdout.write(f"Informations about {hero_name} updated sucessfully")