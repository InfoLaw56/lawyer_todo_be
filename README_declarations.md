download 828(-2) json files - request_test.py
install django 4.1
start project declarations
install django-rest-framework
startapp decl_api
add 'rest_framework', 'decl_api' to settings
create database declaration
pip install psycopg
{
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'declaration',
'USER': 'postgres',
'PASSWORD': 'mzadeba2020',
'HOST': 'localhost',
'PORT': '5432'
}
pip install psycopg2
migrate
create superuser - admin, S@erto2023
create models - Organization, Declaration, Declarant
populate with data except array fields - populate.py
create and populate with data (along with declarations) models - Person, FamilyMember (populate_family.py),
Shareholder, Property (populate_property.py), Movable (populate_movable.py)
skip Securities
create and populate Accounts (populate_accounts.py), Cash (populate_cash.py), Job (populate_jobs.py),
Contract (populate_contracts.py), Gift (populate_gifts.py), InOuts (populate_inouts.py),
EntPartner, Enterprice (populate_enterprices.py)
create GitHub repository...
register Declaration - 'admin.site.register(Declaration)'
create endpoint 'api/all'

pip install django-cors-headers
add "corsheaders", to INSTALLED_APPS
add "corsheaders.middleware.CorsMiddleware", to MIDDLEWARE
add CORS_ALLOW_ALL_ORIGINS = True to settings.py

GIFTS
add fields - decl_id, year, declarant, type_selection - to Gift
edit_gifts.py
'api/gifts' - all gifts

PAGINATION
add decl_api/paginators.py

FILTERING
pip install django-filter
add 'django_filters' to Django's INSTALLED_APPS

GIFTS
create 'api/decl_gifts' - list of declarations where gifts != None
create 'api/declarants' - all declarants
create 'api/organizations' - all organizations
create 'api/declarations_short' - decl_id, submited_at for params - decl_id
create 'api/sum_declaration_gifts' - declarant_id, decl_id, sum_lari params - declarant_id
create 'api/gifts/sum_declarant_gifts', 'api/gifts/sum_gifts_types'.

pupulate gifts types choices - pip install openpyxl, create gift_types.xlsx, create populate_gifts_choices.py

REVIEW
replace 'api/all' with 'api/declarations/all', 'api/decl_gifts' with 'api/declarations/gifts', 'api/sum_declaration_gifts' with 'api/gifts/sum_declaration_gifts'.

create models.Security

add fields decl_id, year, lari

repopulate some tables - populate*cash_1.py, populste_contracts_1.py, populate_enterprices*.py, populate_inouts_1.py, populate_jobs_1.py, populate_movables.py, populate_property.py

pip install pandas
create model Rate

populate_rates.py

populate_gifts_1.py, add_lari_1.py

requests_test_1.py - update_29102023.json

max ids before update: declarations: 54099, bank_accounts: 439049, cash: 16081, contracts: 73018, enterprises: 24134, family_members: 51444, gifts: 2939, inouts: 36137,
jobs: 107661, movables: 36335, properties: 184527.

populate_from_update

daily_rates.py

add_lari_money

check and correct missing declarations - check_missing.py, collect_missing_declarations.py, backup.py, delete_errors.py, pip install progressbar2, new_records.py,
add_lari_2.py, add_lari_money.py

securities - add lari, year to Security, truncate securities, populate_securities.py, populate_securities_from_update

update DB - full_update.py, update_modules/backup_db.py, download_new_declarations.py, new_records.py, gift_types.py, lari_to_money.py, update_daily_rates.py, lari_to_cegij.py

ALTER SEQUENCE organizations_id_seq RESTART WITH 800

JOB

add fields is_declarant, public to models.Job
check_declarant.py
public_jobs.py

add field is_declarant to all models

add fields declarant, person to models.Job - declarant_person_id.py

MISSED IDs - check_culture.py, all_missed.json, list_of_ids.json, missed_ids dir, missed_ids_update.py, missed_ids dir.

add field family_member to models.Job - jobs_family_members.py, jobs_family_members_errors.csv

update 05.01.2024

add field own_id to models.Organization

TRANSFER TO NEW MACHINE

create DB declaration_2024