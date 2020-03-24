# Generated by Django 2.2.7 on 2020-03-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of your Topic.', max_length=600, unique=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('ingredients', models.TextField(help_text='Write the engredients of your Food here.')),
            ],
        ),
    ]