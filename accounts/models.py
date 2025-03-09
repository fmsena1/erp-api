from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission

from companies.models import Enterprise
class UserType(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    OWNER = 'OWNER', 'Owner'
    USER = 'USER', 'User'
    GUEST = 'GUEST', 'Guest'

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    type_user = models.CharField(
        max_length=5,
        choices=UserType.choices,
        default=UserType.USER,
    )

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.email
    
class Group(models.Model):
    name = models.CharField(max_length=150)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name
    

class Group_Permission(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.group} - {self.permission}'
    
class User_Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user} - {self.group}'