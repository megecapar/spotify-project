from django.db import models


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    isCollaborative = models.BooleanField(default=False)
    description = models.TextField(default='')
    url = models.URLField(default='')

    def __str__(self):
        return f"{self.name} => {self.owner} => {self.isCollaborative} => {self.description} => {self.url}"
