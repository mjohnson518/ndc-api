import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime



NDC_TYPE = (
    ('base year emissions goal','BASE YEAR EMISSIONS GOAL'),
    ('fixed-level goal', 'FIXED-LEVEL GOAL'),
    ('base year intensity goal','BASE YEAR INTENSITY GOAL'),
    ('baseline emissions goal','BASELINE EMISSIONS GOAL'),
)

class_rank = (
  ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
)

class NDC(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #country = models.CharField(max_length=75, default='NA')
    title = models.CharField(max_length=100, default='NDC')
    Submission_type = models.CharField(max_length=75, choices=NDC_TYPE, default='base year emissions goal')
    Submission_date = models.DateTimeField(blank=False, default=datetime.date.today)
    Description = models.TextField(max_length=250, blank=False, default='NA')
    NDC_Text = models.FileField(upload_to='static/', max_length=254, default='NA')
    IPFS_CID = models.CharField(max_length=100, default='ipfs.io/')
    ref_num = models.IntegerField(blank=False, default='0')
    slug = models.SlugField(null=False, unique=True, default=uuid.uuid1)

    #CC_Mitigation
    country_name = models.CharField(max_length=75, default='NA')
    country_code = models.CharField(max_length=75, default='NA')

    type_of_target_class = models.IntegerField(blank=False, default=0)
    type_of_target_details = models.CharField(max_length=255, default='NA')

    temp_target_class	= models.CharField(max_length=75, choices=class_rank, default='NA')
    temp_target_details	= models.CharField(max_length=125, default='NA')

    costs_of_ccm_class = models.IntegerField(blank=False, default=0)
    costs_of_ccm_details = models.CharField(max_length=255, default='NA')

    renewable_energy_class = models.IntegerField(blank=False, default=0)
    renewable_energy_details = models.CharField(max_length=255, default='NA')

    energy_efficiency_class = models.IntegerField(blank=False, default=0)
    energy_efficiency_details = models.CharField(max_length=255, default='NA')

    transport_class = models.IntegerField(blank=False, default=0)
    transport_details = models.CharField(max_length=255, default='NA')

    carbon_capture_and_storage_class = models.IntegerField(blank=False, default=0)
    carbon_capture_and_storage_details = models.CharField(max_length=255, default='NA')

    agriculture_class = models.IntegerField(blank=False, default=0)
    agriculture_details = models.CharField(max_length=255, default='NA')

    land_use_and_forestry_class = models.IntegerField(blank=False, default=0)
    land_use_and_forestry_details = models.CharField(max_length=255, default='NA')

    waste_class = models.IntegerField(blank=False, default=0)
    waste_details = models.CharField(max_length=255, default='NA')

    reducing_non_co2_gases_class = models.IntegerField(blank=False, default=0)
    reducing_non_co2_gases_details = models.CharField(max_length=255, default='NA')

    fossil_fuel_production_class = models.IntegerField(blank=False, default=0)
    fossil_fuel_production_details = models.CharField(max_length=255, default='NA')

    fossil_fuel_subsidiaries_class = models.IntegerField(blank=False, default=0)
    fossil_fuel_subsidiaries_details = models.CharField(max_length=255, default='NA')

    land_use_change_class = models.IntegerField(blank=False, default=0)
    land_use_change_details = models.CharField(max_length=255, default='NA')

    redd_class = models.IntegerField(blank=False, default=0)
    redd_details = models.CharField(max_length=255, default='NA')

    trade_class = models.IntegerField(blank=False, default=0)
    trade_details = models.CharField(max_length=255, default='NA')

    market_mechanisms_class = models.IntegerField(blank=False, default=0)
    market_mechanisms_details = models.CharField(max_length=255, default='NA')

    mitigation_documents_class = models.IntegerField(blank=False, default=0)
    mitigation_documents_details = models.TextField(default='NA')

    co_benefits_ccm_class = models.IntegerField(blank=False, default=0)
    co_benefits_ccm_details = models.CharField(max_length=255, default='NA')

#CC_Adaptation

    migration_and_displacement_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    migration_and_displacement_details = models.CharField(max_length=255, default='NA')

    vulnerability_agriculture_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    vulnerability_agriculture_details = models.CharField(max_length=255, default='NA')

    vulnerability_water_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    vulnerability_water_details = models.CharField(max_length=255, default='NA')

    vulnerability_ecosystems_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    vulnerability_ecosystems_details = models.CharField(max_length=255, default='NA')

    vulnerability_health_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    vulnerability_health_details = models.CharField(max_length=255, default='NA')

    vulnerability_coastal_zones_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    vulnerability_coastal_zones_details = models.CharField(max_length=255, default='NA')

    costs_of_recent_climate_related_hazards_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    costs_of_recent_climate_related_hazards_details = models.CharField(max_length=255, default='NA')

    costs_of_future_climate_related_hazards_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    costs_of_future_climate_related_hazards_details = models.CharField(max_length=255, default='NA')

    climate_risks_extreme_weather_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    climate_risks_extreme_weather_details = models.CharField(max_length=255, default='NA')

    climate_risks_floods_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    climate_risks_floods_details = models.CharField(max_length=255, default='NA')

    climate_risks_droughts_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    climate_risks_droughts_details = models.CharField(max_length=255, default='NA')

    climate_risks_temp_increase_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    climate_risks_temp_increase_details = models.CharField(max_length=255, default='NA')

    climate_risks_sea_level_rise_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    climate_risks_sea_level_rise_details = models.CharField(max_length=255, default='NA')

    priority_sectors_water_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    priority_sectors_water_details = models.CharField(max_length=255, default='NA')

    priority_sectors_agriculture_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    priority_sectors_agriculture_details = models.CharField(max_length=255, default='NA')

    priority_sectors_health_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    priority_sectors_health_details = models.CharField(max_length=255, default='NA')

    priority_sectors_ecosystems_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    priority_sectors_ecosystems_details = models.CharField(max_length=255, default='NA')

    priority_sectors_forestry_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    priority_sectors_forestry_details = models.CharField(max_length=255, default='NA')

    quantified_adaptation_targets_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    quantified_adaptation_targets_details = models.CharField(max_length=255, default='NA')

    costs_of_adaptation_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    costs_of_adaptation_details = models.CharField(max_length=255, default='NA')

    adaptation_documents_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    adaptation_documents_details = models.TextField(default='NA')

    co_benefits_of_adaptation_class  = models.CharField(max_length=75, choices=class_rank, default='NA')
    co_benefits_of_adaptation_details = models.CharField(max_length=255, default='NA')

#Fina_and_Support

    conditionality_of_adaptation_finance_class = models.IntegerField(blank=False, default=0)
    conditionality_of_adaptation_finance_details = models.CharField(max_length=255, default='NA')

    conditionality_of_mitigation_finance_class = models.IntegerField(blank=False, default=0)
    conditionality_of_mitigation_finance_details = models.CharField(max_length=255, default='NA')

    technology_needs_class = models.IntegerField(blank=False, default=0)
    technology_needs_details = models.CharField(max_length=255, default='NA')

    conditionality_of_technology_transfer_class = models.IntegerField(blank=False, default=0)
    conditionality_of_technology_transfer_details = models.CharField(max_length=255, default='NA')

    conditionality_of_capacity_building_class = models.IntegerField(blank=False, default=0)
    conditionality_of_capacity_building_details = models.CharField(max_length=255, default='NA')

    means_of_implementation_and_fairness_class = models.IntegerField(blank=False, default=0)
    means_of_implementation_and_fairness_details = models.CharField(max_length=255, default='NA')

    climate_risk_insurance_class = models.IntegerField(blank=False, default=0)
    climate_risk_insurance_details = models.CharField(max_length=255, default='NA')

#Planning_Process

    planning_of_ndc_formulation_class = models.IntegerField(blank=False, default=0)
    planning_of_ndc_formulation_details = models.CharField(max_length=255, default='NA')

    stakeholder_consultation_class = models.IntegerField(blank=False, default=0)
    stakeholder_consultation_details = models.CharField(max_length=255, default='NA')

    education_class = models.IntegerField(blank=False, default=0)
    education_details = models.CharField(max_length=255, default='NA')

    aw_rais_class = models.IntegerField(blank=False, default=0)
    aw_rais_details = models.CharField(max_length=255, default='NA')

    training_class = models.IntegerField(blank=False, default=0)
    training_details = models.CharField(max_length=255, default='NA')

    info_access_class = models.IntegerField(blank=False, default=0)
    info_access_details = models.CharField(max_length=255, default='NA')

    planning_of_ndc_implementation_class = models.IntegerField(blank=False, default=0)
    planning_of_ndc_implementation_details = models.CharField(max_length=255, default='NA')

    monitoring_and_review_class = models.IntegerField(blank=False, default=0)
    monitoring_and_review_details = models.CharField(max_length=255, default='NA')

#Broader_Picture

    sustainable_development_goals_class = models.IntegerField(blank=False, default=0)
    sustainable_development_goals_details = models.CharField(max_length=255, default='NA')

    sustainable_development_class = models.IntegerField(blank=False, default=0)
    sustainable_development_details = models.CharField(max_length=255, default='NA')

    fossil_fuel_subsidy_reform_class = models.IntegerField(blank=False, default=0)
    fossil_fuel_subsidy_reform_details = models.CharField(max_length=255, default='NA')

    green_economy_class = models.IntegerField(blank=False, default=0)
    green_economy_details = models.CharField(max_length=255, default='NA')

    disaster_risk_reduction_class = models.IntegerField(blank=False, default=0)
    disaster_risk_reduction_details = models.CharField(max_length=255, default='NA')

    section_on_fairness_class = models.IntegerField(blank=False, default=0)
    section_on_fairness_details = models.CharField(max_length=255, default='NA')

    historical_responsibility_class = models.IntegerField(blank=False, default=0)
    historical_responsibility_details = models.CharField(max_length=255, default='NA')

    loss_and_damage_class = models.IntegerField(blank=False, default=0)
    loss_and_damage_details = models.CharField(max_length=255, default='NA')

    gender_class = models.IntegerField(blank=False, default=0)
    gender_details = models.CharField(max_length=255, default='NA')

    human_rights_class = models.IntegerField(blank=False, default=0)
    human_rights_details = models.CharField(max_length=255, default='NA')

    income_class = models.IntegerField(blank=False, default=0)
    income_details = models.CharField(max_length=255, default='NA')

    region_id = models.CharField(max_length=75, choices=class_rank, default='NA')
    region_name = models.CharField(max_length=125, default='NA')

    g20_class = models.IntegerField(blank=False, default=0)
    g20_details = models.CharField(max_length=255, default='NA')

    def get_absolute_url(self):
        return reverse("NDC_detail",kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
