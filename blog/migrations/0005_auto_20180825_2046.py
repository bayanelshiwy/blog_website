# Generated by Django 2.0.8 on 2018-08-25 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_remove_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='picture',
            field=models.ImageField(default='default', upload_to=''),
        ),
    ]