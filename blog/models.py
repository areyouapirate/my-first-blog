from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Inscription(models.Model):
    fn_parent = models.CharField(max_length=200)
    sn_parent = models.CharField(max_length=200)
    fn_child = models.CharField(max_length=200)
    sn_child = models.CharField(max_length=200)
    dob_child = models.DateField(null=True, blank=True)
    phone_parent = PhoneNumberField(default='')
    bio_child = models.TextField(blank=True)
    first_choice = models.CharField(max_length=200)
    second_choice = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s %s' % (self.published_date, self.fn_child, self.sn_child, self.dob_child)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    gruppo = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    registration_date = models.DateTimeField(blank=True, null=True)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nomeautore = models.CharField(max_length=500)
    gruppo = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500)
    text = models.TextField()
    approval = models.TextField()
    img = models.ImageField(upload_to='post_img/', blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    last_login = models.DateTimeField(
            default=timezone.now)
    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Place(models.Model):
    typ = models.CharField(max_length=200)
    where = models.CharField(max_length=200)
    coordinates = models.PointField()
    heat = models.CharField(max_length=200)
    capacity = models.IntegerField()
    cost = models.CharField(max_length=200)
    last_group = models.CharField(max_length=200)
    contacts = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    def publish(self):
        self.published_date = timezone.now()
        self.save()