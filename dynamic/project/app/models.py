from django.db import models

# Create your models here.

from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage, RawMediaCloudinaryStorage, VideoMediaCloudinaryStorage

class MediaSubmission(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='images/', storage=MediaCloudinaryStorage(), blank=True, null=True)
    video = models.FileField(upload_to='videos/', storage=VideoMediaCloudinaryStorage(), blank=True, null=True)
    audio = models.FileField(upload_to='audios/', storage=RawMediaCloudinaryStorage(), blank=True, null=True)
    document = models.FileField(upload_to='documents/', storage=RawMediaCloudinaryStorage(), blank=True, null=True)

    def __str__(self):
        return self.title