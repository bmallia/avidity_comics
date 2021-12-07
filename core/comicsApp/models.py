from djongo import models


class Character(models.Model):

    class Meta:
        db_table = 'character'

    _id=models.BigIntegerField(primary_key=True, null=False)

    name=models.CharField(max_length=255, default="")

    description =models.TextField(default="")

    attributionText = models.TextField(default="")

    stories = models.JSONField(default=[]) 

    thumbnail = models.CharField(max_length=500, default="")

    def __str__(self):
        return f"name: {self.name} description: {self.description} thumbnail: {self.thumbnail} attributionText: {self.attributionText} stories: {self.stories}"

    


    
    

