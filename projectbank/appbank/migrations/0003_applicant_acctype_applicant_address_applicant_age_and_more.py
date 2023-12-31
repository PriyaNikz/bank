# Generated by Django 4.2.4 on 2023-08-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbank', '0002_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='acctype',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='branch',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='district',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='gender',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='materials',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
    ]
