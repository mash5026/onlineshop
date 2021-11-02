from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, mobile, address, full_name, password):
        if not email:
            raise ValueError('user must have email')
        if not mobile:
            raise ValueError('user must have mobile')
        if not address:
            raise ValueError('user must have address')
        if not full_name:
            raise ValueError('user must have full name')
        user = self.model(email=self.normalize_email(email), mobile=mobile, address=address, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile, address, full_name, password):
        user = self.create_user(email, mobile, address, full_name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
