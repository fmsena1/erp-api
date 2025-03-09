from django.db import models

class Enterprise(models.Model):
    name = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14, unique=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name