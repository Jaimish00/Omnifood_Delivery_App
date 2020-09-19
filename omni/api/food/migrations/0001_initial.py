# Generated by Django 3.1 on 2020-09-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('price', models.FloatField(default=0, max_length=20)),
                ('is_available', models.BooleanField(blank=True, default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('state_speciality', models.CharField(default=True, max_length=30, null=True)),
                ('schedule_start', models.CharField(choices=[('00:00:00', 'Midnight'), ('01:00:00', '01 AM'), ('02:00:00', '02 AM'), ('03:00:00', '03 AM'), ('04:00:00', '04 AM'), ('05:00:00', '05 AM'), ('06:00:00', '06 AM'), ('07:00:00', '07 AM'), ('08:00:00', '08 AM'), ('09:00:00', '09 AM'), ('10:00:00', '10 AM'), ('11:00:00', '11 AM'), ('12:00:00', 'Noon'), ('13:00:00', '01 PM'), ('14:00:00', '02 PM'), ('15:00:00', '03 PM'), ('16:00:00', '04 PM'), ('17:00:00', '05 PM'), ('18:00:00', '06 PM'), ('19:00:00', '07 PM'), ('20:00:00', '08 PM'), ('21:00:00', '09 PM'), ('22:00:00', '10 PM'), ('23:00:00', '11 PM')], default='00:00:00', max_length=10)),
                ('schedule_end', models.CharField(choices=[('00:00:00', 'Midnight'), ('01:00:00', '01 AM'), ('02:00:00', '02 AM'), ('03:00:00', '03 AM'), ('04:00:00', '04 AM'), ('05:00:00', '05 AM'), ('06:00:00', '06 AM'), ('07:00:00', '07 AM'), ('08:00:00', '08 AM'), ('09:00:00', '09 AM'), ('10:00:00', '10 AM'), ('11:00:00', '11 AM'), ('12:00:00', 'Noon'), ('13:00:00', '01 PM'), ('14:00:00', '02 PM'), ('15:00:00', '03 PM'), ('16:00:00', '04 PM'), ('17:00:00', '05 PM'), ('18:00:00', '06 PM'), ('19:00:00', '07 PM'), ('20:00:00', '08 PM'), ('21:00:00', '09 PM'), ('22:00:00', '10 PM'), ('23:00:00', '11 PM')], default='23:00:00', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]