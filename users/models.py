from django.db import models

# Create your models here.

class AudioFile(models.Model):
    idval = models.IntegerField()
    audio_file = models.FileField(upload_to='audio/') # 'audio/' is a subdirectory within MEDIA_ROOT

class user_details(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    audio_file = models.FileField(
        upload_to='audio/',  # Where uploaded files will go
        default='audio/sample-3s.mp3'  # Path to your default audio file
    )
   #audio_file = models.FileField(upload_to='audio/')


