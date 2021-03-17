from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from apps.access_control.managers import UserAccountManager
from apps.staff.models import Dependent, Department, Job

class UserAccount(AbstractBaseUser):
    # id = models.AutoField()
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    birthdate = models.DateTimeField(null=True, blank=True)
    hire_date = models.DateTimeField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    dependent = models.ForeignKey(Dependent, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    # parent/child relationship
    # Job/UserAccount relationship
    # general idea: foreign key should be placed on the child
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD = 'email'

    #USERNAME_FIELD and password are required by default

    REQUIRED_FIELDS = ['username']

    objects = UserAccountManager()

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True