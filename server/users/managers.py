from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager["User"]):
    def create_user(
        self, email, password=None, is_staff=False, is_active=True, **extra_fields
    ):
        """Create a user instance with the given email and password."""
        email = UserManager.normalize_email(email)
        # Google OAuth2 sends an unnecessary username field
        extra_fields.pop("username", None)

        user = self.model(
            email=email, is_active=is_active, is_staff=is_staff, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )
        # group, created = Group.objects.get_or_create(name="Full Access")
        # if created:
        #    group.permissions.add(*get_permissions())
        # group.user_set.add(user)

    def staff(self):
        return self.get_queryset().filter(is_staff=True)
