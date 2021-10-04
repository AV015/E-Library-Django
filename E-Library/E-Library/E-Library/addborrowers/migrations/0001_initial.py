# Generated by Django 2.2 on 2020-04-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('card_id', models.AutoField(db_column='Card_id', primary_key=True, serialize=False)),
                ('ssn', models.CharField(db_column='Ssn', max_length=9, unique=True)),
                ('bname', models.CharField(blank=True, db_column='Bname', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=14, null=True)),
            ],
            options={
                'db_table': 'borrower',
                'managed': False,
            },
        ),
    ]
