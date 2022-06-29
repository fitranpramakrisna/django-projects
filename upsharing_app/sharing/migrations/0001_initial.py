# Generated by Django 4.0.5 on 2022-06-27 12:18

from django.db import migrations, models
import sharing.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=sharing.models.handle_upload_to)),
            ],
        ),
    ]