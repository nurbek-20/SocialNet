# Generated by Django 5.0.3 on 2024-04-02 12:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_comment_post_alter_comment_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('user', 'target_user')},
        ),
    ]
