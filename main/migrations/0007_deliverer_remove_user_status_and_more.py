# Generated by Django 4.0.4 on 2022-07-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_user_location_user_lat_user_long'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliverer',
            fields=[
                ('tg_id', models.IntegerField(blank=True, null=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('status', models.CharField(blank=True, choices=[('Client', 'Client'), ('Deliverer', 'Deliverer')], max_length=255, null=True)),
                ('username', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.AlterField(
            model_name='order',
            name='image_recipies',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]