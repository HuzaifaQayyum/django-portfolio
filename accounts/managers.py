from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, name, email, password=None, **kwargs):
        """Creates and saves the new user"""
        user = self.model(email=self.normalize_email(email), name=name, **kwargs)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        return self.create_user(name=name, email=email, password=password, **kwargs)
