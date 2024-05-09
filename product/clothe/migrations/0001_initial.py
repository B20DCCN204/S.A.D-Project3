# Generated by Django 4.0.1 on 2024-04-25 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'clothe_type',
            },
        ),
        migrations.CreateModel(
            name='Clothe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='clothe_images/')),
                ('brand', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.BigIntegerField()),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothe.type')),
            ],
            options={
                'db_table': 'clothe',
            },
        ),
    ]