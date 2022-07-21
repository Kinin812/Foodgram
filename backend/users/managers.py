from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(
            self, username, first_name, last_name,
            email, password, **extra_fields
    ):
        if not email:
            raise ValueError("Вы не ввели Email...")
        if not username:
            raise ValueError("Вы не ввели Логин...")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        user = self.model(
            email=email, username=username, first_name=first_name,
            last_name=last_name, **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
            self, email, username, first_name,
            last_name, password, **extra_fields,
    ):

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Отказано в доступе")

        if not extra_fields.get("is_superuser"):
            raise ValueError("Отказано в доступе")

        return self.create_user(
            email=email, username=username, first_name=first_name,
            last_name=last_name, password=password, **extra_fields
        )
