# Generated by Django 3.1.2 on 2020-10-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CC_Mitigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(default='NA', max_length=75)),
                ('country_code', models.CharField(default='NA', max_length=75)),
                ('type_of_target_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('type_of_target_details', models.CharField(default='NA', max_length=125)),
                ('temp_target_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('temp_target_details', models.CharField(default='NA', max_length=125)),
                ('costs_of_ccm_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('costs_of_ccm_details', models.CharField(default='NA', max_length=125)),
                ('renewable_energy_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('renewable_energy_details', models.CharField(default='NA', max_length=125)),
                ('energy_efficiency_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('energy_efficiency_details', models.CharField(default='NA', max_length=125)),
                ('transport_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('transport_details', models.CharField(default='NA', max_length=125)),
                ('carbon_capture_and_storage_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('carbon_capture_and_storage_details', models.CharField(default='NA', max_length=125)),
                ('agriculture_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('agriculture_details', models.CharField(default='NA', max_length=125)),
                ('land_use_and_forestry_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('land_use_and_forestry_details', models.CharField(default='NA', max_length=125)),
                ('waste_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('waste_details', models.CharField(default='NA', max_length=125)),
                ('reducing_non_co2_gases_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('reducing_non_co2_gases_details', models.CharField(default='NA', max_length=125)),
                ('fossil_fuel_production_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('fossil_fuel_production_details', models.CharField(default='NA', max_length=125)),
                ('fossil_fuel_subsidiaries_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('fossil_fuel_subsidiaries_details', models.CharField(default='NA', max_length=125)),
                ('land_use_change_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('land_use_change_details', models.CharField(default='NA', max_length=125)),
                ('redd_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('redd_details', models.CharField(default='NA', max_length=125)),
                ('trade_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('trade_details', models.CharField(default='NA', max_length=125)),
                ('market_mechanisms_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('market_mechanisms_details', models.CharField(default='NA', max_length=125)),
                ('mitigation_documents_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('mitigation_documents_details', models.CharField(default='NA', max_length=125)),
                ('co_benefits_ccm_class', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='NA', max_length=75)),
                ('co_benefits_ccm_details', models.CharField(default='NA', max_length=125)),
            ],
        ),
    ]