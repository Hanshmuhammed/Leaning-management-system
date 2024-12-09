from django.db import models
from user.models import User

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('web_design', 'Web Design'),
        ('graphic_design', 'Graphic Design'),
        ('video_editing', 'Video Editing'),
        ('online_marketing', 'Online Marketing'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})

    def __str__(self):
        return self.title


