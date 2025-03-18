"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user    


class PRO(models.Model):
    name = models.CharField(max_length=100)


class labelAffiliation(models.Model):
        name = models.CharField(max_length=100)

class publisherAffiliation(models.Model):
        name = models.CharField(max_length=100)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    user_role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    pka = models.CharField(max_length=255)
    ipi_number =models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    DOB = models.DateField(blank=True, default='2022-12-03')
    pro = models.ForeignKey(PRO, models.CASCADE, default=None, null=True)
    label_affiliation = models.ForeignKey(labelAffiliation, models.CASCADE, default=None, null=True)
    publisher_affiliation = models.ForeignKey(publisherAffiliation, models.CASCADE, default=None, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

