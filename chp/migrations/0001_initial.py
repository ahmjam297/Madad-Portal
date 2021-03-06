# Generated by Django 2.1.3 on 2019-05-26 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain_department', models.CharField(max_length=100)),
                ('complain_subject', models.CharField(help_text='Enter the complain subject', max_length=100)),
                ('department_head', models.CharField(max_length=100)),
                ('recepient', models.CharField(max_length=100)),
                ('complain_description', models.TextField(max_length=2000)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Not Visited', 'Not Visited'), ('Visited', 'Visited'), ('Inprocess', 'Inprocess'), ('Completed', 'Completed')], max_length=20)),
                ('complain_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
