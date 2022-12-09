from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    profile_img = models.ImageField(default="profile/default.jpeg", upload_to="profile", blank=True)
    introduce = models.TextField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

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
        return self.is_admin

class Pet(models.Model):

    user = models.ForeignKey(User, verbose_name="집사", related_name="user_set", on_delete=models.CASCADE)

    pet_name = models.CharField(verbose_name="펫이름", max_length=100)
    pet_age = models.PositiveIntegerField(verbose_name="펫나이", null=True)
    pet_sex = models.CharField(verbose_name="펫성별", max_length=100, null=True)
    pet_species = models.CharField(verbose_name="품종명", max_length=100,null=True)
    pet_desc = models.CharField(verbose_name="설명", max_length=200)
    pet_image = models.ImageField(default="profile/default.jpeg", upload_to="profile/pet", blank=True)
    
