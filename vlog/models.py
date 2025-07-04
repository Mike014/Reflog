from django.db import models
from cloudinary.models import CloudinaryField

class VlogPost(models.Model):
    title = models.CharField(max_length=200)
    video_file = CloudinaryField('video', resource_type='video', blank=True, null=True)
    audio_note = CloudinaryField('audio', resource_type='video', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    text_reflection = models.TextField()
    # audio_note = models.FileField(upload_to='audio_notes/', blank=True, null=True)
    tags = models.CharField(max_length=200, help_text="Comma-separated tags", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

