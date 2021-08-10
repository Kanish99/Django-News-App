# Generated by Django 3.0.5 on 2020-04-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_place_printingpress'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=12)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='reporter',
            name='address',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reporter',
            name='position',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]