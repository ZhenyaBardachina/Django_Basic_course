# Generated by Django 3.2 on 2021-05-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210511_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='user_avatars'),
        ),
    ]
