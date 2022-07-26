# Generated by Django 4.0.6 on 2022-07-25 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='get_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='image_recipies',
            field=models.ImageField(blank=True, null=True, upload_to='order/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='text_recipies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('Client', 'Client'), ('Deliverer', 'Deliverer')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tg_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
