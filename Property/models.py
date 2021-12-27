from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
import uuid
from django.conf import settings
from django.db.models.fields.related import ManyToManyField
from django.shortcuts import reverse


# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

    objects = models.Manager()
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Role(BaseModel):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name

class User(AbstractBaseUser,BaseModel):
    role = models.ForeignKey(Role,on_delete=models.SET_NULL,null=True)
    full_name = models.CharField(max_length=255,blank=False,null=False)
    email = models.EmailField(unique=True,blank=False,null=False)
    phone_number = models.CharField(max_length=255,blank=False,null=False)
    password =models.CharField(max_length=100,blank=False,null=True)
    receive_notification = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True


class Property(BaseModel):
    seller = models.ForeignKey(User,on_delete=CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=50)
    upload = models.FileField(upload_to="pdf/", null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Apartment_Type(BaseModel):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name
class Property_Detail(BaseModel):
    property = models.ForeignKey(Property,on_delete=CASCADE)
    apartment_type = models.ForeignKey(Apartment_Type,on_delete=CASCADE)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0)
    picture = models.ImageField(upload_to="images/", null=True, blank=True)
    sqft = models.FloatField(null=True)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)

    def __str__(self):
        return str(self.property)


class Contact(BaseModel):
    buyer = models.ForeignKey(User,on_delete=CASCADE,related_name='contact_buyer')
    seller = models.ForeignKey(User,on_delete=CASCADE,related_name='contact_seller',default=True)



class FavouriteProperty(BaseModel):
    buyer = models.ForeignKey(User,on_delete=CASCADE,null=True)
    property = models.ManyToManyField(Property_Detail,related_name='favourite_property',default=None,blank=True)


