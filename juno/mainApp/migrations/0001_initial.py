# Generated by Django 2.1 on 2020-08-20 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.DateTimeField(blank=True, null=True)),
                ('date_ended', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('tags', models.CharField(blank=True, max_length=200, null=True)),
                ('viewers', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Custom_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral', models.CharField(choices=[(1, 'Play Store'), (2, 'Friend')], default=0, max_length=20)),
                ('age', models.CharField(default=0, max_length=20)),
                ('profession', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('motive', models.CharField(choices=[(1, 'Remove Hairs'), (2, 'Regular menses')], default=0, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneOTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(default='91', max_length=8)),
                ('phone_number', models.CharField(blank=True, help_text='Phone number to be validated', max_length=15, unique=True, verbose_name='phone_number')),
                ('otp', models.CharField(help_text='otp to be send to the Phone number', max_length=4, verbose_name='OTP')),
                ('count', models.IntegerField(default=1, help_text='Number of OTP send.', verbose_name='Attempted count')),
                ('is_verified', models.BooleanField(default=False, help_text='If it is true, this means user has validated otp correctly', verbose_name='is_verified')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Object Created date and time', verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'Phone otp',
                'verbose_name_plural': 'Phone otps',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserChallanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_participants', models.IntegerField(blank=True, default=0, null=True)),
                ('challanges', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Challanges')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Custom_User')),
            ],
        ),
        migrations.CreateModel(
            name='UserTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Custom_User')),
            ],
        ),
    ]