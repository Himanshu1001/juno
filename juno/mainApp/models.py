from django.db import models
from django.contrib.auth.models import User


class PhoneOTP(models.Model):
    
    # phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '999999999'")
    country_code = models.CharField(max_length=8, default='91')
    phone_number = models.CharField(verbose_name='phone_number', unique=True, max_length=15, blank=True, help_text="Phone number to be validated") # validators should be a list
    otp = models.CharField(verbose_name='OTP', max_length=4, help_text="otp to be send to the Phone number")
    count = models.IntegerField(verbose_name='Attempted count', default=1, help_text='Number of OTP send.')
    is_verified = models.BooleanField(verbose_name='is_verified', default=False, help_text='If it is true, this means user has validated otp correctly')
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True, help_text="Object Created date and time")

    class Meta:
        managed = True
        verbose_name = 'Phone otp'
        verbose_name_plural = 'Phone otps'

    def __str__(self):
        return "phone: %s - is_verified: %s" %(self.phone_number, self.is_verified)

class Custom_User(models.Model):
    user = models.OneToOneField (
		User,
		on_delete=models.CASCADE,
	)
    Referral_Choices = (
	(1, 'Play Store'),
	(2, 'Friend'),
	)
    referral =  models.CharField(max_length=20, choices=Referral_Choices, default=0)
    age = models.CharField(max_length=20, default=0)
    profession = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    Motive_Choices = (
	(1, 'Remove Hairs'),
	(2, 'Regular menses'),
	)
    motive = models.CharField(max_length=20, choices=Motive_Choices, default=0)


class UserTasks(models.Model):
    user = models.ForeignKey (
		Custom_User,
		on_delete=models.CASCADE,
	)
    tasks = models.CharField(max_length=100,blank=True, null=True,)
    date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)


class Challanges(models.Model):
    date_started = models.DateTimeField(blank=True, null=True)
    date_ended = models.DateTimeField(blank=True, null=True)
    title =  models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # no_of_participants = models.IntegerField(default=0)

class UserChallanges(models.Model):
    user = models.ForeignKey(
        Custom_User,
        on_delete=models.CASCADE,
    )
    challanges = models.ForeignKey(
        Challanges,
        on_delete=models.CASCADE,
    )
    no_of_participants = models.IntegerField(default=0, blank=True, null=True)
    # accepted = models.BooleanField(default=False)

class Content(models.Model):
    image = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=200,blank=True, null=True)
    tags = models.CharField(max_length=200,blank=True, null=True)
    viewers = models.IntegerField(default=0)