from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self ,email , full_name , password):
        if not email:
            raise ValueError('user must have email')

        user = self.model(email=self.normalize_email(email) , full_name=full_name)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self ,email , full_name , password):
        user=self.create_user(email=email , full_name=full_name , password=password)
        user.is_admin=True
        user.save(using=self._db)
        return user