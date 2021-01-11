# Generated by Django 3.1.5 on 2021-01-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pic',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('1', 'Arts'), ('2', 'Technology'), ('3', 'Nature'), ('4', 'Cities')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='allpics/'),
        ),
    ]