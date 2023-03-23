# https://faker.readthedocs.io/en/master/
from faker import Faker
fake = Faker()
name = fake.name()
print(f'Hi, {name}')

addr = fake.address()
print(f' {addr}')

txt = fake.text()
print(f'{txt}')