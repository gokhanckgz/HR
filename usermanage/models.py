from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, user_type, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            user_type=user_type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user




    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username=username,user_type="SU",
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    type_choices = (
        ('SU', 'Super User'),
        ('Company', 'Company User'),
        ('Employe', 'Employe User'),
        ('Supplier', 'Supplier User'),
    )
    user_type = models.CharField(verbose_name='user_type',max_length=10,choices=type_choices,default='Employe')
    username = models.CharField(verbose_name='username',max_length=30,unique=True,)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
    )
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_id(self):
        return self.id

    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.id)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin


