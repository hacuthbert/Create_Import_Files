# https://docs.python.org/3/library/csv.html
# https://faker.readthedocs.io/en/master/
# https://faker.readthedocs.io/en/master/locales/en_US.html
import csv, os, shutil, random
from faker import Faker
from csv import DictWriter


def user_phone():
    phone_number = fake.phone_number()
    if len(phone_number) > 20:
        phone_number = fake.phone_number()
    if len(phone_number) > 20:
        return phone_number[0:20]
    return phone_number


NumberOfRecords = 3
SiteCode = 840000
StartingNumber = 840000


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
UserImport = f'TOTSPC202200100 - import {NumberOfRecords} sites from {StartingNumber} to {SiteCode+NumberOfRecords-1}.csv'
myfile = os.path.join(desktop, UserImport)
fake = Faker()
site_name_suffix = ['Clinical Research Institute', 'Medical Oncology and Hematology, Inc.' , 'University' , 'Medical', 'Medical University', 'Cancer Institute' , 'University Cancer Center', 'Hospital', 'Health System', 'Health Clinic', 'Health', 'Medical Center', 'University Hospital', 'Research Institute', "Children's Hospital", 'School of Medicine', "Women's Hospital", 'Medical Facility', 'Research and Training Hospital', 'Medical Hospital', 'Medical and Dental University', 'Medical and Mental Health Center','Clinic Main Campus', 'Cancer Survival Center', 'Center for Cancer and Blood Disorders', 'Comprehensive Cancer Center', 'Cancer Specialists and Research Institute', 'Cancer Care Alliance', 'Medical College', 'Health Sciences Centre', 'Institute for Medical Research', 'Foundation Trust', 'Heart & Vascular Institute']
addr2_names = ['Investigational Drug Service', 'Department of Pharmacy', 'Investigational Pharmacy Services', 'Medical Research Building', 'Level 2 Pharmacy', 'Clinical Trial Pharmacy', 'Pharmacy Department']
addr3_prefix = ['floor', 'suite', 'building', 'room']
with open(myfile, 'w', newline='') as csvfile:
    fieldnames = ['Site Code', 'Site Name', 'Primary Investigator Prefix', 'Primary Investigator First Name', 'Primary Investigator Last Name', 'Country', 'Time Zone', 'Primary Investigator Phone Number', 'Primary Investigator Email', 'Site Mailing Address Attention', 'Site Mailing Address Street Address', 'Site Mailing Address Address Line 2', 'Site Mailing Address Address Line 3', 'Site Mailing Address City', 'Site Mailing Address State', 'Site Mailing Address Zip', 'Site Shipping Address Attention', 'Site Shipping Address Street Address', 'Site Shipping Address Line 2', 'Site Shipping Address  Line 3', 'Site Shipping Address City', 'Site Shipping Address State', 'Site Shipping Address Zip', 'Site Shipping Address Contact Title', 'Site Shipping Address Contact First Name', 'Site Shipping Address Contact Last Name', 'Site Shipping Address Contact Phone Number', 'Site Shipping Address Contact Email']
    writer: DictWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    n: int
    for n in range(1, NumberOfRecords+1):
        PI_email = f'hacuthbert+SitePI-{SiteCode}@dev.ext'
        if SiteCode % 3 == 0:
            addr2 = random.choice(addr2_names)
            PI_Prefix = f'{fake.prefix_female()}'
            PI_FirstName = f'{fake.first_name_female()}'
            ship_Prefix = f'{fake.prefix_nonbinary()}'
            ship_FirstName = f'{fake.first_name_nonbinary()}'
        else:
            addr2 = ''
        if SiteCode % 7 == 0:
            site_name = f'{fake.city()} {random.choice(site_name_suffix)}'
            addr3 = f'{random.choice(addr3_prefix)} {fake.building_number()}'
            PI_Prefix = f'{fake.prefix_nonbinary()}'
            PI_FirstName = f'{fake.first_name_nonbinary()}'
            ship_Prefix = f'{fake.prefix_male()}'
            ship_FirstName = f'{fake.first_name_male()}'
        else:
            site_name = f'{fake.company()} {random.choice(site_name_suffix)}'
            addr3 = ''
            PI_Prefix = f'{fake.prefix_male()}'
            PI_FirstName = f'{fake.first_name_male()}'
            ship_Prefix = f'{fake.prefix_female()}'
            ship_FirstName = f'{fake.first_name_female()}'
        ship_LastName = f'{fake.last_name()}'
        shipping_email = f'{ship_FirstName}.{ship_LastName}@dev.ext'
        writer.writerow({'Site Code': SiteCode, 'Site Name': site_name, 'Primary Investigator Prefix': PI_Prefix, 'Primary Investigator First Name': PI_FirstName, 'Primary Investigator Last Name': fake.last_name(), 'Country': 'United States', 'Time Zone': '(UTC-05:00) Eastern Time (US & Canada)', 'Primary Investigator Phone Number': user_phone(), 'Primary Investigator Email': PI_email, 'Site Mailing Address Attention': fake.name(), 'Site Mailing Address Street Address': fake.street_address(), 'Site Mailing Address Address Line 2': addr2, 'Site Mailing Address Address Line 3': addr3, 'Site Mailing Address City': fake.city(), 'Site Mailing Address State': fake.state_abbr(), 'Site Mailing Address Zip': fake.postcode(), 'Site Shipping Address Attention': fake.name(), 'Site Shipping Address Street Address': fake.street_address(), 'Site Shipping Address Line 2': addr2, 'Site Shipping Address  Line 3': addr3, 'Site Shipping Address City': fake.city(), 'Site Shipping Address State': fake.state_abbr(), 'Site Shipping Address Zip': fake.postcode(), 'Site Shipping Address Contact Title':  ship_Prefix, 'Site Shipping Address Contact First Name': ship_FirstName, 'Site Shipping Address Contact Last Name': ship_LastName, 'Site Shipping Address Contact Phone Number': user_phone(), 'Site Shipping Address Contact Email': shipping_email})
        SiteCode += 1
        