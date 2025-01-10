from myfirstapp.models import College, Student
from faker import Faker
import random

fake = Faker("en_IN")

# List of college names
college_names = [
    "Indian Institute of Technology",
    "Vellore Institute of Technology",
    "National Institute of Technology",
    "Silicon Valley Institute of Technology",
    "Manipal Institute of Technology",
]


def dbSeeder(records=20) -> None:
    # Ensure we have some colleges to choose from
    if not College.objects.count():
        # Seed some colleges if none exist
        for name in college_names:
            College.objects.create(college_name=name, college_address=fake.address())

    for i in range(records):
        college = random.choice(College.objects.all())
        gender_choice = random.choice(["Male", "Female"])
        name = fake.name()
        mobile_number = fake.phone_number()[:12]
        email = fake.email()
        gender = gender_choice
        age = random.randint(18, 25)
        student_bio = fake.text()

        Student.objects.create(
            college=college,
            name=name,
            mobile_number=mobile_number,
            email=email,
            gender=gender,
            # age=age,
            student_bio=student_bio,
            date_of_birth=fake.date_between(start_date="-30y", end_date="-18y"),
            # student_profile_image=fake.image_path(category="avatar"),
            student_file=fake.file_path(depth=3, category=None),
            # created_at=fake.date_time_this_decade(before_today=True),
            # updated_at=fake.date_time_this_decade(after_today=False),
        )
