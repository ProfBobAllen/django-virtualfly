# Generated by Django 2.2.13 on 2020-07-13 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vflies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherID', models.IntegerField()),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]