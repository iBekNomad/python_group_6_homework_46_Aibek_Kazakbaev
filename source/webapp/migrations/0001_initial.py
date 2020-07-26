# Generated by Django 2.2.13 on 2020-07-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], default='new', max_length=15, verbose_name='Новая')),
                ('text', models.TextField(default='', max_length=3000, null=True, verbose_name='Подробное описание')),
                ('created_at', models.DateField(default='', verbose_name='Дата создания')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]