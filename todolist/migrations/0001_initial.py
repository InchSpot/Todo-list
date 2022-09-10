# Generated by Django 4.1.1 on 2022-09-09 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('HP', 'Высокий приоритет'), ('MP', 'Средний приоритет'), ('LP', 'Низкий приоритет')], default='HP', max_length=100)),
            ],
            options={
                'verbose_name': 'Priority',
                'verbose_name_plural': 'Priorities',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Pn', 'В ожидании выполнения'), ('D', 'Выполнено'), ('IP', 'Выполняется')], default='Pn', max_length=100)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2022-09-09')),
                ('due_date', models.DateField(default='2022-09-09')),
                ('priority', models.ForeignKey(default='general', on_delete=django.db.models.deletion.PROTECT, to='todolist.priority')),
                ('status', models.ForeignKey(default='general', on_delete=django.db.models.deletion.PROTECT, to='todolist.status')),
            ],
            options={
                'ordering': ['-due_date'],
            },
        ),
    ]