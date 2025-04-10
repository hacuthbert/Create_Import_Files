# https://docs.python.org/3/library/csv.html
# https://faker.readthedocs.io/en/master/
# https://faker.readthedocs.io/en/master/providers/faker.providers.address.html
import csv, os, shutil, random
from faker import Faker
from csv import DictWriter

NumberOfRecords = 30


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
parameter_set = f'release nnk in Canada.csv'
myfile = os.path.join(desktop, parameter_set)
fake = Faker()
with open(myfile, 'w', newline='') as csvfile:
    fieldnames = ['Username', 'Password', 'Protocol', 'supply_type', 'Supply_Location', 'NonnumberedKitType', 'NonnumberedKitTypeQuantity', 'orderingLotNumberBox', 'labelLotNumberBox', 'Status', 'ExpiryDate', 'Country_Select', 'Expiry_Canada', 'Status_Canada', 'AuditableTransaction_SelectedReason']
    writer: DictWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    n: int
    for n in range(1, NumberOfRecords+1):
        lot_number = f'{fake.country_code()}{random.randrange(10, 99)}'
        if n % 2 == 0:
            NonnumberedKitType = 'C - Kit Type C'
            orderingLotNumberBox = f'{lot_number}-C-OL'
            labelLotNumberBox = f'{lot_number}-C-LL'
        else:
            NonnumberedKitType = 'D - Kit Type D'
            orderingLotNumberBox = f'{lot_number}-D-OL'
            labelLotNumberBox = f'{lot_number}-D-LL'
        writer.writerow({'Username': 'Username', 'Password': 'Password', 'Protocol': 'Protocol', 'supply_type': 'Nonnumbered', 'Supply_Location': 'Canada Distribution Center, CAN (CAN1)', 'NonnumberedKitType': NonnumberedKitType, 'NonnumberedKitTypeQuantity': '996', 'orderingLotNumberBox': orderingLotNumberBox, 'labelLotNumberBox': labelLotNumberBox, 'Status': 'Shipping Released', 'ExpiryDate': '31 Jan 2030', 'Country_Select': 'Canada', 'Expiry_Canada': '31 Jan 2030', 'Status_Canada': 'Released', 'AuditableTransaction_SelectedReason': 'Other'})
        