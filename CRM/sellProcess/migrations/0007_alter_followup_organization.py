# Generated by Django 3.2.5 on 2021-08-09 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_alter_organization_organization_name'),
        ('sellProcess', '0006_alter_followup_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization', verbose_name='For Organization'),
        ),
    ]
