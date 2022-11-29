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
    enrollment_type = models.CharField(max_length=15, blank=True, default="")
    date_administered = models.DateField(blank=True, default="2022-09-20")

    middle_name = models.CharField(max_length=50, blank=True, default="")
    extension = models.CharField(max_length=12, blank=True, default="")
    sex = models.IntegerField(blank=True, default=0)
    
    date_of_birth = models.CharField(max_length=100, blank=True, default="")
    place_of_birth = models.CharField(max_length=100, blank=True, default="")
    civil_status = models.CharField(max_length=20, blank=True, default="")

    educational_attainment = models.CharField(max_length=50, blank=True, default="")
    is_pwd = models.IntegerField(blank=True, default=0)
    is_4ps_beneficiary = models.IntegerField(blank=True, default=0)
    is_ip = models.IntegerField(blank=True, default=0)

    # FARM PROFILE
    main_livelihood = models.CharField(max_length=50, blank=True, default="")
    livelihood_product = models.CharField(max_length=50, blank=True, default="")
    laborer_activity = models.CharField(max_length=50, blank=True, default="")
    fishing_activity = models.CharField(max_length=50, blank=True, default="")
    involvement_type = models.CharField(max_length=50, blank=True, default="")

    ownership_document_name = models.CharField(max_length=100, blank=True, default="")
    ownership_document = models.TextField(blank=True, default="")
    signature_name = models.CharField(max_length=100, blank=True, default="")
    signature = models.TextField(blank=True, default="")
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username", "password", "role"]

    def __str__(self):
        return self.email
