# Generated by Django 4.2.5 on 2025-03-27 01:36

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('cliente', 'Cliente'), ('mecanico', 'Mecânico'), ('fornecedor', 'Fornecedor')], max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='custom_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='MecanicoProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=500)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('level', models.CharField(choices=[('Bronze', 'Bronze'), ('Prata', 'Prata'), ('Ouro', 'Ouro')], default='Bronze', max_length=20)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('score', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mecanico_profile', to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='FornecedorProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fornecedor_profile', to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='ClienteProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(max_length=500)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('score', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_profile', to='users.user')),
            ],
        ),
    ]
