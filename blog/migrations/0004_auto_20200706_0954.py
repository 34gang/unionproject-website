# Generated by Django 3.0.5 on 2020-07-06 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='isi',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Dibuat_Pada',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='nama',
            new_name='name',
        ),
    ]