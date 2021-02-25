# Generated by Django 3.1 on 2021-02-25 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='uploader_of_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_image', to=settings.AUTH_USER_MODEL),
        ),
    ]