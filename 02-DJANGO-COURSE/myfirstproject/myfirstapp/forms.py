from django import forms
from myfirstapp.models import Student, Student2

#! Approach - 1
class DjangoStudentForm(forms.Form):
    name = forms.CharField(max_length=50)
    age = forms.IntegerField(min_value=18, max_value=100)


#! Approach - 2
class DjangoModelStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ["name", "gender", "email", "student_bio", ]
        exclude = ["date_of_birth", "student_profile_image", "student_file"]