# Generated by Django 2.2.5 on 2019-11-04 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Life', '0002_auto_20191103_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='picture',
            field=models.ImageField(null=True, upload_to='department/'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='picture',
            field=models.ImageField(null=True, upload_to='doctors/'),
        ),
        migrations.AlterField(
            model_name='department',
            name='hod',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Life.Department'),
        ),
    ]