from django.db import models
from django.core.exceptions import ValidationError
import re
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(unique=True)
    resume = models.FileField(upload_to='resumes/')

    def clean(self):
        errors = {}

        # Name validation
        if not self.name.isalpha():
            errors['name'] = "Name must contain only alphabets"
        elif len(self.name) < 3 or len(self.name) > 10:
            errors['name'] = "Name must be between 3 and 10 characters"

        # Age validation
        if self.age < 18 or self.age > 60:
            errors['age'] = "Age must be between 18 and 60"

        # Email validation
        if not self.email.endswith("@gmail.com"):
            errors['email'] = "Only Gmail email allowed"

        # Phone validation
        if not re.match(r'^[6-9]\d{9}$', self.phone):
            errors['phone'] = "Enter a valid Indian mobile number"

         # Password validation - at least 1 number
        if not any(char.isdigit() for char in self.password):
            errors['password'] = "Password must contain at least one number"
            
        # Resume validation
        if self.resume:
            if not self.resume.name.endswith(('.pdf', '.docx')):
                errors['resume'] = "Only PDF or DOCX files allowed"
            elif self.resume.size > 2 * 1024 * 1024:
                errors['resume'] = "Resume size must be under 2 MB"

        # Raise all errors together
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()   # ensures validation runs even on objects.create()
        super().save(*args, **kwargs)


class Task(models.Model):
    task = models.CharField()