# Generated by Django 4.1.3 on 2022-11-26 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorHospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=25)),
                ('hospital_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField()),
                ('Location', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='StrokeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('hypertension', models.IntegerField()),
                ('heartdisease', models.IntegerField()),
                ('avgglucoselevel', models.IntegerField()),
                ('bmi', models.IntegerField()),
                ('genderMale', models.IntegerField()),
                ('genderOther', models.IntegerField()),
                ('evermarriedYes', models.IntegerField()),
                ('worktypeNeverworked', models.IntegerField()),
                ('worktypePrivate', models.IntegerField()),
                ('worktypeSelfemployed', models.IntegerField()),
                ('worktypechildren', models.IntegerField()),
                ('ResidencetypeUrban', models.IntegerField()),
                ('smokingstatusformerlysmoked', models.IntegerField()),
                ('smokingstatusneversmoked', models.IntegerField()),
                ('smokingstatussmokes', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('probability', models.FloatField(null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
