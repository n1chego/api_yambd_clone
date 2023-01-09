from django.contrib.auth.models import AbstractUser
from django.db import models


USER = 'USER'
ADMIN = 'ADMIN'
MODER = 'MODER'
ROLES = (
    (USER, 'user'),
    (ADMIN, 'admin'),
    (MODER, 'moderator'),
)


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True
    )
    role = models.CharField(
        choices=ROLES,
        default=USER,
        max_length=6
    )
