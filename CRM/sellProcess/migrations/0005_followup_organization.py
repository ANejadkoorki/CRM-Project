# Generated by Django 3.2.5 on 2021-08-09 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_alter_organization_organization_name'),
        ('sellProcess', '0004_followup'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup',
            name='organization',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='organization.organization', verbose_name='For Organization'),
            preserve_default=False,
        ),
    ]