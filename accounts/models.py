from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager # AbstractBaseUser= See notes, BaseUserManager= inspect different premission.and give permission.

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None): # create_user ar moddha chaila kiso field pass kora jai and it's name is must create user.
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email), # normalize_email= 1. max@gamil.com = 2.Max@gamil.Com , so that case sensetive na.
            username = username, # amader model ar username k override korce , user j email deyasa seta diya.
            first_name = first_name, # amader model ar first_name k override korce , user j first_name deyasa seta diya.
            last_name = last_name, # amader model ar last_name k override korce , user j last_name deyasa seta diya. 
        )

        user.set_password(password) # user j password ta dibe seta create_user model ar moddha pass korlam.
        user.save(using=self._db) # custome usre create korer somoy save korer jonno using=self._db use kora hoi.
        return user # fianly user k return kora holo..

    def create_superuser(self, first_name, last_name, email, username, password): # first_name,last_name,email, username,password makes superuser more secure.
        user = self.create_user(
            email = self.normalize_email(email), 
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)  # custome usre create korer somoy save korer jonno using=self._db use kora hoi.
        return user



class Account(AbstractBaseUser): # ai Account , Account name show korbe data base a ,karon  amra user k Account dara override korce.
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True) # user name unique hobe.
    email           = models.EmailField(max_length=100, unique=True) #email unique hobe.
    phone_number    = models.CharField(max_length=50) 
    pro_picture     = models.ImageField(upload_to='photos/profile_picture', blank=True)

    # required
    date_joined     = models.DateTimeField(auto_now_add=True) 
    last_login      = models.DateTimeField(auto_now=True) 
    is_admin        = models.BooleanField(default=False) # ai permission golo admin chaila pora deta parbe.
    is_staff        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=False)
    is_superadmin        = models.BooleanField(default=False) 

    USERNAME_FIELD = 'email' # user name field uaer ar poriborte email thakbe.
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None): 
        return self.is_admin

    def has_module_perms(self, add_label): # gives some permissions.
        return True

class WishListProduct(models.Model):
    id=models.IntegerField(primary_key=True)
    wish_product_slug=models.SlugField(max_length=200, unique=True, null=True)
    wish_product_name=models.CharField(max_length=100)
    wish_product_price=models.IntegerField()
    wish_product_image=models.ImageField()
    wish_product_description=models.CharField(max_length=100)
    wish_product_created_date=models.DateTimeField(auto_now_add=True)