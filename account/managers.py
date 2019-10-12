from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Manager object for custom user class.
    """

    def create_superuser(self, *args, **kwargs):
        """
        Create a user with superuser privileges.
        Args:
            *args:
                The positional args to pass to ``create_user``.
            **kwargs:
                The keyword args to pass to ``create_user``.
        Returns:
            The new user instance.
        """
        return self.create_user(
            *args,
            is_staff=True,
            is_superuser=True,
            **kwargs,
        )

    def create_user(self, name, username, password=None, **kwargs):
        """
        Create a new user.
        Args:
            name:
                The user's full name.
            username:
                The user's username.
            password:
                The user's password.
            **kwargs:
                Additional keyword arguments to pass to the model
                instance.
        Returns:
            The new user instance.
        """
        user = self.model(name=name, username=username, **kwargs)
        user.set_password(password)
        user.save()

        return user 