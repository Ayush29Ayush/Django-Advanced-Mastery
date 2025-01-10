from django.db import models


class College(models.Model):
    college_name = models.CharField(max_length=100)
    college_address = models.CharField(max_length=100)


class Student(models.Model):
    gender_choices = (("Male", "Male"), ("Female", "Female"))
    college = models.ForeignKey(
        College, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=gender_choices, default="Male")
    student_bio = models.TextField()
    date_of_birth = models.DateField(blank=True, null=True)
    student_profile_image = models.ImageField(
        null=True, blank=True, upload_to="student/"
    )
    student_file = models.FileField(null=True, blank=True, upload_to="files/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.author_name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(
        max_length=100,
    )
    published_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "book_table"
        ordering = ("-price", "book_name")
        verbose_name = "Book"
        verbose_name_plural = "Book"


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    country = models.CharField(default="IN", max_length=100)

    def __str__(self):
        return self.brand_name

    class Meta:
        unique_together = ("brand_name", "country")
        indexes = [models.Index(fields=["brand_name", "country"])]


class SkillManager(models.Manager):

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_deleted=False)


class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    objects = SkillManager()
    new_manager = models.Manager()

    def __str__(self):
        return self.skill_name


class Person(models.Model):
    person_name = models.CharField(max_length=100)
    skill = models.ManyToManyField(Skills)

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, null=True, blank=True)
    upload_file = models.FileField(null=True, blank=True, upload_to="files/")