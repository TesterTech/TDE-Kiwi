# Generated by Django 3.0.2 on 2020-01-20 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('testplans', '0007_notifications_default_true'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltestplan',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='historicaltestplan',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True),
        ),

        # drop TestPlan.plan_id in favor of TestPlan.id
        migrations.AlterIndexTogether(
            name='testplan',
            index_together=set(),
        ),
        migrations.RenameField(
            model_name='testplan',
            old_name='plan_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='historicaltestplan',
            old_name='plan_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='testplan',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historicaltestplan',
            name='id',
            field=models.IntegerField(auto_created=True, blank=True,
                                      db_index=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='plantype',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True,
                                   serialize=False, verbose_name='ID'),
        ),
    ]
