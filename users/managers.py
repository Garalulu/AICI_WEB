from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where usr_id is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, usr_id, password, name, uid, **extra_fields):
        """
        Create and save a user with the given usr_id, password, name and uid.
        """
        if not usr_id:
            raise ValueError(_("The user id must be set"))
        
        if not name:
            raise ValueError(_("The name must be set"))
        
        '''if not phonenum:
            raise ValueError(_("The phone number must be set"))'''
        
        if not uid:
            raise ValueError(_("The engineer id must be set"))
        
        
        from .models import UidTB  # Import inside the method to avoid circular import


        try:
            uid_instance = UidTB.objects.get(uid=uid) # Change uid to UidTB instance for matching with forein key correctly.
        except UidTB.DoesNotExist:
            raise ValueError(_("Invalid engineer id"))
        
        user = self.model(usr_id=usr_id, name=name, uid=uid_instance, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, usr_id, password, name, uid, **extra_fields):
        """
        Create and save a SuperUser with the given usr_id, password, name and uid.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(usr_id, password, name, uid, **extra_fields)