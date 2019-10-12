import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


from account import managers



class User(PermissionsMixin, AbstractBaseUser):
    """
    A single user.
    """
    REQUIRED_FIELDS = ['name']
    USERNAME_FIELD = 'username'

    id = models.UUIDField(
        default=uuid.uuid4,
        help_text=_('A unique identifier for the user.'),
        primary_key=True,
        unique=True,
        verbose_name=_('ID'),
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_('A boolean indicating if the user account is active. '
                    'Inactive accounts cannot perform actions on the site.'),
        verbose_name=_('is active'),
    )
    is_staff = models.BooleanField(
        default=False,
        help_text=_('A boolean indicating if the user is allowed to access '
                    'the admin site.'),
        verbose_name=_('is staff'),
    )
    is_superuser = models.BooleanField(
        default=False,
        help_text=_('A boolean indicating if the user has all permissions '
                    'without them being explicitly granted.'),
        verbose_name=_('is superuser'),
    )
    name = models.CharField(
        help_text=_("The user's name."),
        max_length=100,
        verbose_name=_('full name'),
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('The time the user was created.'),
        verbose_name=_('time created'),
    )
    time_updated = models.DateTimeField(
        auto_now=True,
        help_text=_('The time the user was last updated.'),
        verbose_name=_('time updated'),
    )
    username = models.CharField(
        help_text=_('The name the user logs in as.'),
        max_length=100,
        unique=True,
        verbose_name=_('username'),
    )
    email = models.EmailField(
        help_text=_('email to contact user'),
        max_length=200,
        unique=True,
        verbose_name=_('email'),
        )
    phone = PhoneNumberField(
        help_text=_('phone number to which menu will be texted'),
        null=False, 
        blank=False, 
        unique=True,
        verbose_name=_('phone number'))

    # Custom Manager
    objects = managers.UserManager()

    class Meta:
        ordering = ('time_created',)
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __repr__(self):
        """
        Get a string representation of the user.
        Returns:
            A string containing the information required to reconstruct
            the user.
        """
        return f'User(id={self.id:r}, username={self.username:r})'

    def __str__(self):
        """
        Get a string identifying the user.
        Returns:
            The user's name.
        """
        return self.name