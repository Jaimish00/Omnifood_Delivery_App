from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
import datetime, jwt, time

# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def get_by_natural_key(self, email):
#         return self.get(email=email)

# class CustomerManager(BaseUserManager):
#     use_in_migrations = True

#     def create_customer(self, name, email, phone, address, session_token=0, password=None):
#         if email is None:
#             raise TypeError('Users must have an email address.')
#         customer = Customer(name=name, 
#                             email=self.normalize_email(email),
#                             phone=phone, address=address, 
#                             session_token=session_token)
#         customer.set_password(password)
#         customer.save()
#         return customer

# class HotelAdminManager(BaseUserManager):
#     use_in_migrations = True

#     def create_hotel_admin(self, name, email, phone, hotel_address, hotel_decription, 
#                         hotel_email, hotel_phone, fssai_license, session_token=0, password=None):
#         if email is None:
#             raise TypeError('Users must have an email address.')
#         h_admin = HotelAdmin(name=name, 
#                             email=self.normalize_email(email),
#                             phone=phone, hotel_address=hotel_address,
#                             hotel_decription=hotel_decription,
#                             hotel_email=hotel_email, hotel_phone=hotel_phone,
#                             fssai_license=fssai_license, 
#                             session_token=session_token)
#         h_admin.set_password(password)
#         h_admin.save()
#         return h_admin

# class DeliveryPersonManager(BaseUserManager):
#     use_in_migrations = True

#     def create_delivery_person(self, name, email, phone, preferred_location, date_of_birth, 
#                         gender, license_plate_no, driving_license_number, session_token=0, password=None):
#         if email is None:
#             raise TypeError('Users must have an email address.')
        
#         d_person = DeliveryPerson(name=name, 
#                             email=self.normalize_email(email),
#                             phone=phone, preferred_location=preferred_location,
#                             date_of_birth=date_of_birth,
#                             gender=gender, license_plate_no=license_plate_no,
#                             driving_license_number=driving_license_number, 
#                             session_token=session_token)
        
#         d_person.set_password(password)
#         d_person.save()
#         return d_person




class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=70, unique=True, blank=False)
    name = models.CharField(max_length=50, default='Anonymous')
    phone = models.CharField(max_length=10, blank=True, null=True)# Blank specifies that this field can go empty in database
    session_token = models.CharField(max_length=10, default=0)

    username = None
    # username = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email' #username field will be governed by email. by default it is username
    REQUIRED_FIELDS = []
    
    # objects = UserManager()

    # @property
    # def token(self):
    #     dt = datetime.now()
    #     token = jwt.encode({
    #         'id': self.id,
    #         'exp': int(time.mktime(dt.timetuple()))
    #     }, settings.SECRET_KEY, algorithm='HS256')
    #     return token.decode('utf-8')

    def get_name(self):
        return self.name

    def __str__(self):
        return self.email


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer', default=None)
    address = models.CharField(max_length=500, blank=True, null=True)
   
    # objects = CustomerManager()

    def __str__(self):
        return self.user.name
    
    # TODO: Order integration

class HotelAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='hotel_admin', default=None)
    hotel_name = models.CharField(max_length=100, default='Random', blank=True)
    hotel_address = models.CharField(max_length=500, blank=True, null=True)
    hotel_description = models.CharField(max_length=2000, blank=True, null=True)
    hotel_email = models.EmailField(verbose_name='Hotel Email', max_length=60, unique=True)
    hotel_phone = models.CharField(max_length=10, blank=True, null=True)
    fssai_license = models.CharField(max_length=14, blank=True, null=True)
    

    # objects = HotelAdminManager()

    def __str__(self):
        return self.user.name
    
    # TODO: Order integration


LOCATION_CHOICES = (
    ('bombay', 'Bombay'),
	('ahemdabad', 'Ahemdabad'),
	('delhi', 'Delhi'),
	('surat', 'Surat'),
	('chennai', 'Chennai'),
	('banglore', 'Banglore'),
	('jaipur', 'Jaipur'),
	('pune', 'Pune'),
	('hyderabad', 'Hyderabad'),
)

class DeliveryPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='delivery_person', default=None)
    preferred_location = models.CharField(max_length=10, choices=LOCATION_CHOICES, default='ahemdabad')
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    license_plate_no = models.CharField(max_length=10, blank=True, null=True)
    driving_license_number = models.CharField(max_length=16, blank=True, null=True)

    # objects = DeliveryPersonManager()

    def __str__(self):
        return self.user.name
    
    # TODO: Order integration



