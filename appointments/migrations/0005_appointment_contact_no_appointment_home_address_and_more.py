# Generated by Django 5.1.5 on 2025-02-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_appointment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='contact_no',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='appointment',
            name='home_address',
            field=models.TextField(default='Not provided'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='parent_guardian',
            field=models.CharField(default='Not provided', max_length=100),
        ),
        migrations.AddField(
            model_name='appointment',
            name='types_of_client',
            field=models.CharField(choices=[('student', 'Student'), ('personnel', 'Personnel'), ('non_bu_personnel', 'Non-BU Personnel (e.g., part-timers)'), ('others', 'Others (guests)')], default='student', max_length=20),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='purpose',
            field=models.CharField(choices=[('medical', 'Medical (consultation & treatment)'), ('physical_examination', 'Physical examination (e.g., athletic activities, OJT/internship, extra-curricular, scholarship)'), ('dental', 'Dental consultation & treatment'), ('vaccination', 'Vaccination (Flu & Pneumonia) done annually (free)')], max_length=20),
        ),
    ]
