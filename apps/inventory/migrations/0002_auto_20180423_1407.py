# Generated by Django 2.0.4 on 2018-04-23 14:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Inventory',
                'verbose_name_plural': 'Inventories',
            },
        ),
        migrations.CreateModel(
            name='InventoryCheckPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date & time')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Inventory', verbose_name='Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryCPQty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('check_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.InventoryCheckPoint', verbose_name='Check point')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='inventory.Inventory', verbose_name='Inventory')),
            ],
            options={
                'verbose_name': 'Inventory transaction',
                'verbose_name_plural': 'Inventory transactions',
                'ordering': ['-date', '-id'],
            },
        ),
        migrations.CreateModel(
            name='ItemTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=64, verbose_name='Description')),
                ('brand', models.CharField(blank=True, max_length=32, null=True, verbose_name='Brand')),
                ('model', models.CharField(blank=True, max_length=32, null=True, verbose_name='Model')),
                ('part_number', models.CharField(blank=True, max_length=32, null=True, verbose_name='Part number')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'Item template',
                'verbose_name_plural': 'Item templates',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('address_line1', models.CharField(blank=True, max_length=64, null=True, verbose_name='Address')),
                ('address_line2', models.CharField(blank=True, max_length=64, null=True, verbose_name='Address')),
                ('address_line3', models.CharField(blank=True, max_length=64, null=True, verbose_name='Address')),
                ('address_line4', models.CharField(blank=True, max_length=64, null=True, verbose_name='Address')),
                ('phone_number1', models.CharField(blank=True, max_length=32, null=True, verbose_name='Phone number')),
                ('phone_number2', models.CharField(blank=True, max_length=32, null=True, verbose_name='Phone number')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timedate', models.DateTimeField(auto_now_add=True, verbose_name='Date & time')),
                ('action', models.CharField(max_length=32, verbose_name='Action')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('address_line1', models.CharField(blank=True, max_length=64, null=True, verbose_name='Address')),
                ('address_line2', models.CharField(blank=True, max_length=64, null=True, verbose_name='Address')),
                ('address_line3', models.CharField(blank=True, max_length=64, null=True, verbose_name='Address')),
                ('address_line4', models.CharField(blank=True, max_length=64, null=True, verbose_name='Address')),
                ('phone_number1', models.CharField(blank=True, max_length=32, null=True, verbose_name='Phone number')),
                ('phone_number2', models.CharField(blank=True, max_length=32, null=True, verbose_name='Phone number')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='inventorytransaction',
            name='supply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ItemTemplate', verbose_name='Supply'),
        ),
        migrations.AddField(
            model_name='inventorycpqty',
            name='supply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ItemTemplate', verbose_name='Supply'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Location', verbose_name='Location'),
        ),
    ]