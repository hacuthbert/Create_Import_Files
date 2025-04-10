#https://faker.readthedocs.io/en/master/providers/baseprovider.html
from faker import Faker
fake = Faker()
Faker.seed(0)
for _ in range(20):
    print(f'{fake.bothify(text='???###-LL', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')}')
