from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # Add related_name to avoid clashes with the default auth.User model
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Customize the related_name to avoid conflict
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Customize the related_name to avoid conflict
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


