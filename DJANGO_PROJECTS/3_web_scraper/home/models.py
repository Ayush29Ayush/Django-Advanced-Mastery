from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(blank=True, null=True)
    image_path = models.FilePathField(path="media/imdb_images_downloads/", null=True, blank=True)
    external_link = models.URLField()

    def __str__(self):
        return self.title
    
class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    
    # Gender choices
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('P', 'Prefer not to say'),
    ]
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_adult = models.BooleanField(default=False)  

    def save(self, *args, **kwargs):
        # Automatically set is_adult based on age
        self.is_adult = self.age >= 18
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name