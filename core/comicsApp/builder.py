import requests

from core.comicsApp.models import Character
from core.comicsApp.authentication import AuthSingleton


class Director():

    def __init__(self, builder):
        self._builder = builder

    
    def construct_character(self):
        self._builder.create_new_character()
        self._builder.find_characters_stories()
        self._builder.store_characters_image()

    def get_character(self):
        return self._builder.character


class Builder():

    def __init__(self):
        self.character = None

    def create_new_character(self):
        pass

    def find_characters_stories(self):
        pass

    def store_characters_image(self):
        pass

class CharacterBuilder(Builder):
    """
        This class constructs the object with about the character searched.
        The constructed information is:
        The story's description
        A list of names and pictures of the characters that feature in the story
         The Marvel attribution text

    """
    def __init__(self, name, model=None, progress_bar=None):
        self.hero_name = name
        self.characterModel = Character()
        self.stories = set()
        self.character_ids = set()
        self.progress_bar = progress_bar

        try:
            print(f"Fetch data from https://gateway.marvel.com:443/v1/public/characters?name={name}&apikey={AuthSingleton().public_key}&ts={AuthSingleton().timestamp}&hash={AuthSingleton().hash}")
            res1 = requests.get(f"https://gateway.marvel.com:443/v1/public/characters?name={name}&apikey={AuthSingleton().public_key}&ts={AuthSingleton().timestamp}&hash={AuthSingleton().hash}")
        except requests.exceptions.ConnectionError as e:
            print("Connection erro while getting the character's mavel information")
            exit(1)

            
        if res1 and res1.status_code != 200:
            print(f"Error while retriving data, status code {res1.status_code}")
            exit(2)
        
        self.data =  res1.json()
        
        if not self.data:
            print(f"No data found! for {hero_name}")
            exit(0)
    
    def create_new_character(self):
        """
            Populates the object with the story's description and the Marvel attributioni text
        """
        results = self.data['data']['results']
        for result in results:

            char_filtered = Character.objects.filter(name=self.hero_name)
            thumb = result['thumbnail']['path'] + '/portrait_xlarge.' + result['thumbnail']['extension']

            storie_items = result['stories']['items']
            for story in storie_items:
                   id_story = story['resourceURI'].rsplit('/', 1)[-1]
                   self.stories.add(id_story) 

            if char_filtered.exists():
                char_filtered.update(description=result['description'], attributionText=self.data['attributionText'], stories=result['stories']['items'], thumbnail=thumb)
                ##self.characterModel = char_filtered
                print(f"Character updated!")
            else:
                character = Character(_id=result['id'], name=result["name"], description=result['description'], attributionText=self.data['attributionText'], thumbnail=thumb)
                character.save()
                ##self.characterModel = character     
                print(f"Character saved")
        self.progress_bar.update(30)
    
    def find_characters_stories(self):
        """
            Add stories ids from character searched
        """
        print(f"Finding stories for {self.stories}")

        for storyid in self.stories:
            url = f"https://gateway.marvel.com/v1/public/stories/{storyid}?apikey={AuthSingleton().public_key}&ts={AuthSingleton().timestamp}&hash={AuthSingleton().hash}"
            
            res = requests.get(url)

            if res.status_code == 200: 
                json_data = res.json()
                results = json_data['data']['results']
                
                for result in results:
                    for character in result['characters']['items']:
                        resourceURI= character['resourceURI'].rsplit('/', 1)[-1]
                        self.character_ids.add(resourceURI)
            self.progress_bar.update(65)

    def store_characters_image(self):
        """  Store the characters stories image """
        characters_stores = []

        print(f"store the characters {self.character_ids}")
        
        for character in self.character_ids:
            url = f"http://gateway.marvel.com/v1/public/characters/{character}?apikey={AuthSingleton().public_key}&ts={AuthSingleton().timestamp}&hash={AuthSingleton().hash}"
            res = requests.get(url)
            ##print(url)
            if res.status_code == 200:
                json_data = res.json()
                results = json_data['data']['results']
                for result in results:
                    thumbnail = result['thumbnail']
                    path = f"{thumbnail['path']}/portrait_small.{thumbnail['extension']}"
                    characters_stores.append({"url": path, "name": result['name']})
            character_resulted = Character.objects.filter(_id=character)
            character_resulted.update(stories=characters_stores)

        self.progress_bar.update(100)      
                    

                