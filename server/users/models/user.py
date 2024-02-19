from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models.team import Team
from uuid import uuid4


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    email = models.EmailField("Email address", unique=True, blank=False)
    username = models.CharField(max_length=32, unique=True, blank=True)
    given_name = models.CharField("Given name", max_length=64, blank=True)
    family_name = models.CharField("Family name", max_length=64, blank=True)
    city = models.CharField("City", max_length=128)
    country = models.CharField("Country", max_length=128)
    favorite_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="Team")
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    # language_code = models.CharField(max_length=35, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)
    locale = models.CharField(max_length=16)  # ISO language code (e.g., "en" or "zh-Hans")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)
    last_visit = models.DateTimeField(auto_now=True, editable=True)
    last_verify_email_request = models.DateTimeField(null=True, blank=True)
    last_password_reset_request = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
