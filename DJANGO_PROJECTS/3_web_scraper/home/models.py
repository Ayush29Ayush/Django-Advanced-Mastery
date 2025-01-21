from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(blank=True, null=True)
    image_path = models.FilePathField(path="media/imdb_images_downloads/", null=True, blank=True)
    external_link = models.URLField()

    def __str__(self):
        return self.title