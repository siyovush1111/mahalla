from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser



class MyUserManager(BaseUserManager):


    def create_user(self, username, password=None, **extra_fields):c
        user = self.model(username, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user


    def _create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser need to have is_staff=True.')
        if extra_fields.get('is_suoeruser'):
            raise ValueError('Supeeruser need to have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('sector_leader', 'Sektor rajbari'),
        ('nighborhood_leader', 'Mahalla rahbari'),
        ('measurs', "Hokim"),
        ('admin', 'Admin'),
    )
    first_name = models.CharField(verbose_name='Ism', max_length=250, blank=True)
    last_name = models.CharField(verbose_name="Familiya", max_length=250, blank=True)
    email = models.EmailField(verbose_name="Pochta", max_length=250, blank=True)
    username = models.CharField(verbose_name='username', max_length=250, unique=True)
    is_staff = models.BooleanField(verbose_name='Hodimlarning holati', default=False)
    is_active = models.BooleanField(verbose_name="Faol", default=True)
    birthdate = models.DateField(verbose_name="Tug'ilgan sanasi",
                                 null=True, blank=True)
    phone = models.CharField(
        verbose_name="Telefon raqami",
        max_length=250,
        null=True,
        blank=True
    )
    user_type = models.CharField(
        verbose_name="Foydalanuvchi turi",
        max_length=250,
        choices=USER_TYPE,
        default="nighborhood_leader"
    )
    neighborhood = models.ForeignKey("mahalla.Neighborhood", verbose_name="qaysi mahalla rahbari",
                                     on_delete=models.SET_NULL, null=True, blank=True)
    sector = models.ForeignKey("mahalla.Sector", verbose_name='Qaysi sektor rahbari?',
                               on_delete=models.SET_NULL, null=True, blank=True)



    USER_FIELD = 'username'
    objects = MyUserManager()


    def __str__(self):
        return self.username


    def get_full_name(self):
        return f"ism {self.first_name} familiya {self.last_name}"


    def get_short_name(self):
        return self.first_name


    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Fydalanuvchilar"








