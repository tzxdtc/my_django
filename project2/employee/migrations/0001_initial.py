# Generated by Django 2.0 on 2018-08-26 02:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='department')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='FirstName')),
                ('last_name', models.CharField(max_length=20, verbose_name='LastName')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.Department', verbose_name='department')),
            ],
        ),
    ]