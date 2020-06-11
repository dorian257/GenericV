from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin


# Create your models here.

class MYUserManager(BaseUserManager):

    def create_user(self,request,email,username,password=None):

        if not email:
            raise ValueError("Users must have an Email")

        if not username:
            raise ValueError("Users must have a username")

        if email:
            email = self.normalize_email(email)


        user = self.model(email=email,username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,request,email,username,password=None):

        if not email:
            raise ValueError("Superusers must have an Email")

        if not username:
            raise ValueError("Superusers must have a username")

        user = self.create_user(email,username,password)
        user.is_admin=True
        user.save(using=self._db)

        return user


class MyUser(AbstractBaseUser,PermissionsMixin):

    email = models.CharField(max_length=50,verbose_name='Email adresse',unique=True)
    username = models.CharField(max_length=27,verbose_name='Akazina',unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MYUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    def __str__(self):
        """
        Returns a string representation of this 'User'.

        This string is used when a 'User' is printed in the console.
        """
        return getattr(self, self.USERNAME_FIELD)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Profil():

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    proffesion = models.CharField(max_length=20)

    def get_full_name(self):
        name = self.first_name
        name += " " +self.last_name

        return name

    def get_short_name(self):

        return self.first_name


