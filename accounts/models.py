"""Account database."""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionMixin, UserManager)


class User(AbstractBaseUser, PermissionMixin):
    """User Table."""

    username = models.CharField('Nome de usuário', max_length=30, unique=True)
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('É ativo', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['email']

    def __str__(self):
        """Default string."""
        return self.name or self.username

    def get_short_name(self):
        """Get short name."""
        return self.username

    def get_full_name(self):
        """Get Full name."""
        return str(self)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
