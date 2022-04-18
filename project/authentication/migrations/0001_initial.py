# Generated by Django 4.0.4 on 2022-04-18 19:41

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name=' شماره تماس ')),
                ('address', models.CharField(blank=True, max_length=3000, null=True, verbose_name=' آدرس  ')),
                ('photo', models.ImageField(blank=True, default='user/photo/default.png', null=True, upload_to='user/photo', verbose_name='تصویر کاربر')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پروفایل',
                'verbose_name_plural': ' پروفایل ها ',
            },
        ),
    ]