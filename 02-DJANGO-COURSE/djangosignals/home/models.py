from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from PIL import Image
import os


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=(("Male", "Male"), ("Female", "Female")))
    student_id = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.student_name
    
class ImageModel(models.Model):
    original_image = models.ImageField(upload_to="images/")  # Images are uploaded to 'media/images/'
    thumbnail_mini = models.ImageField(upload_to="images/thumbnails", null=True, blank=True)  # Thumbnails in 'media/images/thumbnails/'
    thumbnail_small = models.ImageField(upload_to="images/thumbnails", null=True, blank=True)
    thumbnail_medium = models.ImageField(upload_to="images/thumbnails", null=True, blank=True)
    thumbnail_large = models.ImageField(upload_to="images/thumbnails", null=True, blank=True)

@receiver(post_save, sender=ImageModel)
def create_thumbnails(sender, instance, created, **kwargs):
    if created:
        sizes = {
            "thumbnail_mini": (50, 50),
            "thumbnail_small": (100, 100),
            "thumbnail_medium": (300, 300),
            "thumbnail_large": (600, 600)
        }

        # Open the original image
        img = Image.open(instance.original_image.path)

        # Get the base path for thumbnails, which should be 'media/images/thumbnails/'
        thumbnail_dir = os.path.join('media', 'images', 'thumbnails')

        # Ensure the 'images/thumbnails/' directory exists
        if not os.path.exists(thumbnail_dir):
            os.makedirs(thumbnail_dir)

        for field, size in sizes.items():
            # Resize the image
            img.thumbnail(size, Image.Resampling.LANCZOS)
            
            # Prepare the path and filename (using os.path.splitext to extract the base name and extension)
            thumb_name, thumb_extension = os.path.splitext(instance.original_image.name)
            thumb_filename = f"{thumb_name}_{size[0]}X{size[1]}{thumb_extension.lower()}"
            
            # Correctly create the thumbnail path in 'media/images/thumbnails/'
            thumb_path = os.path.join('images', 'thumbnails', thumb_filename)  # This ensures it's relative to MEDIA_ROOT

            # Save the thumbnail to the filesystem
            img.save(os.path.join(settings.MEDIA_ROOT, thumb_path))  # Save the image in the 'media' folder

            # Set the corresponding thumbnail field
            setattr(instance, field, thumb_path)

        # Save the instance with the updated thumbnail paths
        instance.save()

    
@receiver(pre_save, sender=Student)    
def pre_save_student(sender, instance, **kwargs):
    print("Student object is about to be saved...")
    
@receiver(post_save, sender=Student)
def save_student(sender, instance, created, **kwargs):
    print(sender, instance)
    print(created)
    if created:
        instance.student_id = f"STU-000{instance.id}"
        instance.save()
    print("Student object created...")
    
@receiver(pre_delete, sender=Student)
def pre_delete_student(sender, instance, **kwargs):
    print("Student object is about to be deleted...")
    
@receiver(post_delete, sender=Student)
def post_delete_student(sender, instance, **kwargs):
    print("Student object deleted...")