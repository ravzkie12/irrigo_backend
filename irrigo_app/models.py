from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    # REGISTRATION / REQUIRED FIELDS
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=100, default="123")
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    role = models.CharField(max_length=50)
    # PERSONAL INFORMATION
    enrollment_type = models.CharField(max_length=15, null=True, blank=True)
    date_administered = models.DateField(null=True, blank=True, default="2022-09-20")

    middle_name = models.CharField(max_length=50, null=True, blank=True)
    extension = models.CharField(max_length=12, null=True, blank=True)
    sex = models.IntegerField(blank=True, null=True, default=0)
    
    date_of_birth = models.DateField(null=True, blank=True, default="2022-09-20")
    place_of_birth = models.CharField(max_length=100, null=True, blank=True)
    civil_status = models.CharField(max_length=20, null=True, blank=True)

    educational_attainment = models.CharField(max_length=50, null=True, blank=True)
    is_pwd = models.IntegerField(null=True, blank=True, default=0)
    is_4ps_beneficiary = models.IntegerField(null=True, blank=True, default=0)
    is_ip = models.IntegerField(null=True, blank=True, default=0)

    # FARM PROFILE
    main_livelihood = models.CharField(max_length=50, null=True, blank=True)
    livelihood_product = models.CharField(max_length=50, null=True, blank=True)
    laborer_activity = models.CharField(max_length=50, null=True, blank=True)
    fishing_activity = models.CharField(max_length=50, null=True, blank=True)
    involvement_type = models.CharField(max_length=50, null=True, blank=True)

    ownership_document = models.TextField(null=True, blank=True)
    signature = models.TextField(null=True, blank=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username", "password", "role"]

    def __str__(self):
        return self.email
