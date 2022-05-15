# Generated by Django 4.0.4 on 2022-05-15 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('content_libraries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_posts', to='accounts.client'),
        ),
    ]