# Generated by Django 4.2.4 on 2023-09-06 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    def create_default_priorities(apps, schema_editor):
        Priority = apps.get_model('home', 'Priority')
        Priority.objects.create(id=1, name='Baja')
        Priority.objects.create(id=2, name='Media')
        Priority.objects.create(id=3, name='Alta')

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RunPython(create_default_priorities),
        migrations.AddField(
            model_name='task',
            name='task_priority',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.priority'),
        ),
    ]
