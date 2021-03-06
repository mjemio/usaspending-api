from django.db import models
from usaspending_api.common.models import DataSourceTrackedModel


class RefCityCountyCode(models.Model):
    city_county_code_id = models.AutoField(primary_key=True)
    state_code = models.CharField(max_length=2, blank=True, null=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=5, blank=True, null=True)
    county_code = models.CharField(max_length=3, blank=True, null=True)
    county_name = models.CharField(max_length=100, blank=True, null=True)
    type_of_area = models.CharField(max_length=20, blank=True, null=True)
    valid_begin_date = models.DateTimeField(blank=True, null=True)
    valid_end_date = models.DateTimeField(blank=True, null=True)
    valid_code_indicator = models.CharField(max_length=1, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'ref_city_county_code'


class RefCountryCode(models.Model):
    country_code = models.CharField(primary_key=True, max_length=3)
    country_name = models.CharField(max_length=100, blank=True, null=True)
    valid_begin_date = models.DateTimeField(blank=True, null=True)
    valid_end_date = models.DateTimeField(blank=True, null=True)
    valid_code_indicator = models.CharField(max_length=1, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'ref_country_code'


"""{
    'agency_name': 'name',
    'agency_code_fpds': 'fpds_code',
    'agency_code_cgac': 'cgac_code',
    'department_parent_id': 'department',
    'sub_tier_parent_id': 'parent_agency',
    'agency_code_aac': 'acc_code',
    'agency_code_4cc': 'fourcc_code',

    }"""


class Agency(models.Model):
    # id = models.AutoField(primary_key=True)
    id = models.AutoField(primary_key=True)  # meaningless id
    cgac_code = models.CharField(max_length=3, blank=True, null=True, verbose_name="Agency Code")
    # agency_code_aac = models.CharField(max_length=6, blank=True, null=True)
    fpds_code = models.CharField(max_length=4, blank=True, null=True)
    # will equal fpds_code if a top level department
    subtier_code = models.CharField(max_length=4, blank=True, null=True, verbose_name="Sub-Tier Agency Code")
    name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Agency Name")
    department = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='sub_departments')
    parent_agency = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='sub_agencies')
    aac_code = models.CharField(max_length=6, blank=True, null=True, verbose_name="Office Code")
    fourcc_code = models.CharField(max_length=4, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    location = models.ForeignKey('Location', models.DO_NOTHING, null=True)

    class Meta:
        managed = True
        db_table = 'agency'

    def __str__(self):
        if self.department:
            return "%s - %s" % (self.department.name or '', self.name)
        else:
            return "%s" % (self.name)


class Location(DataSourceTrackedModel):
    location_id = models.AutoField(primary_key=True)
    location_country_code = models.ForeignKey('RefCountryCode', models.DO_NOTHING, db_column='location_country_code', blank=True, null=True, verbose_name="Country Code")
    location_country_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Country Name")
    location_state_code = models.CharField(max_length=2, blank=True, null=True, verbose_name="State Code")
    location_state_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="State Name")
    location_state_text = models.CharField(max_length=100, blank=True, null=True)
    # Changed by KPJ to 100 from 40, on 20161013
    location_city_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="City Name")
    location_city_code = models.CharField(max_length=5, blank=True, null=True)
    location_county_name = models.CharField(max_length=40, blank=True, null=True)
    location_county_code = models.CharField(max_length=3, blank=True, null=True)
    location_address_line1 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Address Line 1")
    location_address_line2 = models.CharField(max_length=150, blank=True, null=True, verbose_name="Address Line 2")
    location_address_line3 = models.CharField(max_length=55, blank=True, null=True, verbose_name="Address Line 3")
    location_foreign_location_description = models.CharField(max_length=100, blank=True, null=True)
    location_zip4 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ZIP+4")
    location_zip_4a = models.CharField(max_length=10, blank=True, null=True)
    location_congressional_code = models.CharField(max_length=2, blank=True, null=True,  verbose_name="Congressional District Code")
    location_performance_code = models.CharField(max_length=9, blank=True, null=True, verbose_name="Primary Place Of Performance Location Code")
    location_zip_last4 = models.CharField(max_length=4, blank=True, null=True)
    location_zip5 = models.CharField(max_length=5, blank=True, null=True)
    location_foreign_postal_code = models.CharField(max_length=50, blank=True, null=True)
    location_foreign_province = models.CharField(max_length=25, blank=True, null=True)
    location_foreign_city_name = models.CharField(max_length=40, blank=True, null=True)
    reporting_period_start = models.DateField(blank=True, null=True)
    reporting_period_end = models.DateField(blank=True, null=True)
    last_modified_date = models.DateField(blank=True, null=True)
    certified_date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        # Let's make almost every column unique together so we don't have to
        # perform heavy lifting on checking if a location already exists or not
        unique_together = ("location_country_code",
                           "location_country_name",
                           "location_state_code",
                           "location_state_name",
                           "location_state_text",
                           "location_city_name",
                           "location_city_code",
                           "location_county_name",
                           "location_county_code",
                           "location_address_line1",
                           "location_address_line2",
                           "location_address_line3",
                           "location_foreign_location_description",
                           "location_zip4",
                           "location_congressional_code",
                           "location_performance_code",
                           "location_zip_last4",
                           "location_zip5",
                           "location_foreign_postal_code",
                           "location_foreign_province",
                           "location_foreign_city_name",
                           "reporting_period_start",
                           "reporting_period_end")


class LegalEntity(DataSourceTrackedModel):
    legal_entity_id = models.AutoField(primary_key=True)
    location = models.ForeignKey('Location', models.DO_NOTHING, null=True)
    ultimate_parent_legal_entity_id = models.IntegerField(null=True)
    # duns number ?
    recipient_name = models.CharField(max_length=120, blank=True, verbose_name="Recipient Name")
    vendor_doing_as_business_name = models.CharField(max_length=400, blank=True, null=True)
    vendor_phone_number = models.CharField(max_length=30, blank=True, null=True)
    vendor_fax_number = models.CharField(max_length=30, blank=True, null=True)
    business_types = models.CharField(max_length=3, blank=True, null=True)
    recipient_unique_id = models.CharField(max_length=9, blank=True, null=True, verbose_name="DUNS Number")
    limited_liability_corporation = models.CharField(max_length=1, blank=True, null=True)
    sole_proprietorship = models.CharField(max_length=1, blank=True, null=True)
    partnership_or_limited_liability_partnership = models.CharField(max_length=1, blank=True, null=True)
    subchapter_scorporation = models.CharField(max_length=1, blank=True, null=True)
    foundation = models.CharField(max_length=1, blank=True, null=True)
    for_profit_organization = models.CharField(max_length=1, blank=True, null=True)
    nonprofit_organization = models.CharField(max_length=1, blank=True, null=True)
    corporate_entity_tax_exempt = models.CharField(max_length=1, blank=True, null=True)
    corporate_entity_not_tax_exempt = models.CharField(max_length=1, blank=True, null=True)
    other_not_for_profit_organization = models.CharField(max_length=1, blank=True, null=True)
    sam_exception = models.CharField(max_length=1, blank=True, null=True)
    city_local_government = models.CharField(max_length=1, blank=True, null=True)
    county_local_government = models.CharField(max_length=1, blank=True, null=True)
    inter_municipal_local_government = models.CharField(max_length=1, blank=True, null=True)
    local_government_owned = models.CharField(max_length=1, blank=True, null=True)
    municipality_local_government = models.CharField(max_length=1, blank=True, null=True)
    school_district_local_government = models.CharField(max_length=1, blank=True, null=True)
    township_local_government = models.CharField(max_length=1, blank=True, null=True)
    us_state_government = models.CharField(max_length=1, blank=True, null=True)
    us_federal_government = models.CharField(max_length=1, blank=True, null=True)
    federal_agency = models.CharField(max_length=1, blank=True, null=True)
    federally_funded_research_and_development_corp = models.CharField(max_length=1, blank=True, null=True)
    us_tribal_government = models.CharField(max_length=1, blank=True, null=True)
    foreign_government = models.CharField(max_length=1, blank=True, null=True)
    community_developed_corporation_owned_firm = models.CharField(max_length=1, blank=True, null=True)
    labor_surplus_area_firm = models.CharField(max_length=1, blank=True, null=True)
    small_agricultural_cooperative = models.CharField(max_length=1, blank=True, null=True)
    international_organization = models.CharField(max_length=1, blank=True, null=True)
    us_government_entity = models.CharField(max_length=1, blank=True, null=True)
    emerging_small_business = models.CharField(max_length=1, blank=True, null=True)
    c8a_program_participant = models.CharField(db_column='8a_program_participant', max_length=1, blank=True, null=True, verbose_name="8a Program Participant")  # Field renamed because it wasn't a valid Python identifier.
    sba_certified_8a_joint_venture = models.CharField(max_length=1, blank=True, null=True)
    dot_certified_disadvantage = models.CharField(max_length=1, blank=True, null=True)
    self_certified_small_disadvantaged_business = models.CharField(max_length=1, blank=True, null=True)
    historically_underutilized_business_zone = models.CharField(max_length=1, blank=True, null=True)
    small_disadvantaged_business = models.CharField(max_length=1, blank=True, null=True)
    the_ability_one_program = models.CharField(max_length=1, blank=True, null=True)
    historically_black_college = models.CharField(max_length=1, blank=True, null=True)
    c1862_land_grant_college = models.CharField(db_column='1862_land_grant_college', max_length=1, blank=True, null=True, verbose_name="1862 Land Grant College")  # Field renamed because it wasn't a valid Python identifier.
    c1890_land_grant_college = models.CharField(db_column='1890_land_grant_college', max_length=1, blank=True, null=True, verbose_name="1890 Land Grant College")  # Field renamed because it wasn't a valid Python identifier.
    c1994_land_grant_college = models.CharField(db_column='1994_land_grant_college', max_length=1, blank=True, null=True, verbose_name="1894 Land Grant College")  # Field renamed because it wasn't a valid Python identifier.
    minority_institution = models.CharField(max_length=1, blank=True, null=True)
    private_university_or_college = models.CharField(max_length=1, blank=True, null=True)
    school_of_forestry = models.CharField(max_length=1, blank=True, null=True)
    state_controlled_institution_of_higher_learning = models.CharField(max_length=1, blank=True, null=True)
    tribal_college = models.CharField(max_length=1, blank=True, null=True)
    veterinary_college = models.CharField(max_length=1, blank=True, null=True)
    educational_institution = models.CharField(max_length=1, blank=True, null=True)
    alaskan_native_servicing_institution = models.CharField(max_length=1, blank=True, null=True, verbose_name="Alaskan Native Owned Servicing Institution")
    community_development_corporation = models.CharField(max_length=1, blank=True, null=True)
    native_hawaiian_servicing_institution = models.CharField(max_length=1, blank=True, null=True)
    domestic_shelter = models.CharField(max_length=1, blank=True, null=True)
    manufacturer_of_goods = models.CharField(max_length=1, blank=True, null=True)
    hospital_flag = models.CharField(max_length=1, blank=True, null=True)
    veterinary_hospital = models.CharField(max_length=1, blank=True, null=True)
    hispanic_servicing_institution = models.CharField(max_length=1, blank=True, null=True)
    woman_owned_business = models.CharField(max_length=1, blank=True, null=True)
    minority_owned_business = models.CharField(max_length=1, blank=True, null=True)
    women_owned_small_business = models.CharField(max_length=1, blank=True, null=True)
    economically_disadvantaged_women_owned_small_business = models.CharField(max_length=1, blank=True, null=True)
    joint_venture_women_owned_small_business = models.CharField(max_length=1, blank=True, null=True)
    joint_venture_economic_disadvantaged_women_owned_small_bus = models.CharField(max_length=1, blank=True, null=True)
    veteran_owned_business = models.CharField(max_length=1, blank=True, null=True)
    service_disabled_veteran_owned_business = models.CharField(max_length=1, blank=True, null=True)
    contracts = models.CharField(max_length=1, blank=True, null=True)
    grants = models.CharField(max_length=1, blank=True, null=True)
    receives_contracts_and_grants = models.CharField(max_length=1, blank=True, null=True)
    airport_authority = models.CharField(max_length=1, blank=True, null=True, verbose_name="Airport Authority")
    council_of_governments = models.CharField(max_length=1, blank=True, null=True)
    housing_authorities_public_tribal = models.CharField(max_length=1, blank=True, null=True)
    interstate_entity = models.CharField(max_length=1, blank=True, null=True)
    planning_commission = models.CharField(max_length=1, blank=True, null=True)
    port_authority = models.CharField(max_length=1, blank=True, null=True)
    transit_authority = models.CharField(max_length=1, blank=True, null=True)
    foreign_owned_and_located = models.CharField(max_length=1, blank=True, null=True)
    american_indian_owned_business = models.CharField(max_length=1, blank=True, null=True, verbose_name="American Indian Owned Business")
    alaskan_native_owned_corporation_or_firm = models.CharField(max_length=1, blank=True, null=True, verbose_name="Alaskan Native Owned Corporation or Firm")
    indian_tribe_federally_recognized = models.CharField(max_length=1, blank=True, null=True)
    native_hawaiian_owned_business = models.CharField(max_length=1, blank=True, null=True)
    tribally_owned_business = models.CharField(max_length=1, blank=True, null=True)
    asian_pacific_american_owned_business = models.CharField(max_length=1, blank=True, null=True, verbose_name="Asian Pacific American Owned business")
    black_american_owned_business = models.CharField(max_length=1, blank=True, null=True)
    hispanic_american_owned_business = models.CharField(max_length=1, blank=True, null=True)
    native_american_owned_business = models.CharField(max_length=1, blank=True, null=True)
    subcontinent_asian_asian_indian_american_owned_business = models.CharField(max_length=1, blank=True, null=True)
    other_minority_owned_business = models.CharField(max_length=1, blank=True, null=True)
    us_local_government = models.CharField(max_length=1, blank=True, null=True)
    undefinitized_action = models.CharField(max_length=1, blank=True, null=True)
    domestic_or_foreign_entity = models.CharField(max_length=1, blank=True, null=True)
    division_name = models.CharField(max_length=100, blank=True, null=True)
    division_number = models.CharField(max_length=100, blank=True, null=True)
    last_modified_date = models.DateField(blank=True, null=True)
    certified_date = models.DateField(blank=True, null=True)
    reporting_period_start = models.DateField(blank=True, null=True)
    reporting_period_end = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'legal_entity'
        unique_together = (('recipient_name'),)


# Reference tables
class RefObjectClassCode(models.Model):
    object_class = models.CharField(primary_key=True, max_length=4)
    max_object_class_name = models.CharField(max_length=60, blank=True, null=True)
    direct_or_reimbursable = models.CharField(max_length=25, blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    valid_begin_date = models.DateTimeField(blank=True, null=True)
    valid_end_date = models.DateTimeField(blank=True, null=True)
    valid_code_indicator = models.CharField(max_length=1, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'ref_object_class_code'


"""BD 09/21 - Added the ref_program_activity_id, responsible_agency_id, allocation_transfer_agency_id,main_account_code to the RefProgramActivity model as well as unique concatenated key"""


class RefProgramActivity(models.Model):
    ref_program_activity_id = models.IntegerField(primary_key=True)
    program_activity_code = models.CharField(max_length=4)
    program_activity_name = models.CharField(max_length=164)
    budget_year = models.CharField(max_length=4, blank=True, null=True)
    responsible_agency_id = models.CharField(max_length=3, blank=True, null=True)
    allocation_transfer_agency_id = models.CharField(max_length=3, blank=True, null=True)
    main_account_code = models.CharField(max_length=4, blank=True, null=True)
    valid_begin_date = models.DateTimeField(blank=True, null=True)
    valid_end_date = models.DateTimeField(blank=True, null=True)
    valid_code_indicator = models.CharField(max_length=1, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'ref_program_activity'
        unique_together = (('program_activity_code', 'budget_year', 'responsible_agency_id', 'allocation_transfer_agency_id', 'main_account_code'),)


class CFDAProgram(DataSourceTrackedModel):
    program_number = models.CharField(primary_key=True, max_length=7)
    program_title = models.TextField(blank=True, null=True)
    popular_name = models.TextField(blank=True, null=True)
    federal_agency = models.TextField(blank=True, null=True)
    authorization = models.TextField(blank=True, null=True)
    objectives = models.TextField(blank=True, null=True)
    types_of_assistance = models.TextField(blank=True, null=True)
    uses_and_use_restrictions = models.TextField(blank=True, null=True)
    applicant_eligibility = models.TextField(blank=True, null=True)
    beneficiary_eligibility = models.TextField(blank=True, null=True)
    credentials_documentation = models.TextField(blank=True, null=True)
    pre_application_coordination = models.TextField(blank=True, null=True)
    application_procedures = models.TextField(blank=True, null=True)
    award_procedure = models.TextField(blank=True, null=True)
    deadlines = models.TextField(blank=True, null=True)
    range_of_approval_disapproval_time = models.TextField(blank=True, null=True)
    website_address = models.TextField(blank=True, null=True)
    formula_and_matching_requirements = models.TextField(blank=True, null=True)
    length_and_time_phasing_of_assistance = models.TextField(blank=True, null=True)
    reports = models.TextField(blank=True, null=True)
    audits = models.TextField(blank=True, null=True)
    records = models.TextField(blank=True, null=True)
    account_identification = models.TextField(blank=True, null=True)
    obligations = models.TextField(blank=True, null=True)
    range_and_average_of_financial_assistance = models.TextField(blank=True, null=True)
    appeals = models.TextField(blank=True, null=True)
    renewals = models.TextField(blank=True, null=True)
    program_accomplishments = models.TextField(blank=True, null=True)
    regulations_guidelines_and_literature = models.TextField(blank=True, null=True)
    regional_or_local_office = models.TextField(blank=True, null=True)
    headquarters_office = models.TextField(blank=True, null=True)
    related_programs = models.TextField(blank=True, null=True)
    examples_of_funded_projects = models.TextField(blank=True, null=True)
    criteria_for_selecting_proposals = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    recovery = models.TextField(blank=True, null=True)
    omb_agency_code = models.TextField(blank=True, null=True)
    omb_bureau_code = models.TextField(blank=True, null=True)
    # published_date = models.DateTimeField(blank=True, null=True)
    # archived_date = models.DateTimeField(blank=True, null=True)
    published_date = models.TextField(blank=True, null=True)
    archived_date = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'cfda_program'

    def __str__(self):
        return "%s" % (self.program_title)
