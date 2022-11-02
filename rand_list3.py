# https://docs.python.org/3/library/csv.html
import csv
from csv import DictWriter

def threes(value):
  last_digit = int(repr(value)[-1])
  if last_digit % 3 == 0:
    return "3"
  elif last_digit % 2 == 0:
    return "2"
  else:
    return "1"

with open('RandList.csv', 'w', newline='') as csvfile:
    fieldnames = ['Randomization number', 'Treatment Code', 'Sequence Number', 'Cohort Code']
    writer: DictWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    n: int
    BlockSize = 4
    NumberOfBlocks = 50
    BlockNumber = 1
    SequenceNumber = 2000
    RandomizationNumber = 11000
    BlockNumber = 1000

    for n in range(1, NumberOfBlocks+1):
        BlockNumber += 1
        OneOfThree = threes(BlockNumber)
        TreatmentArm = "TA" + OneOfThree
        Cohort = "Cohort " + OneOfThree
        for j in range(1, BlockSize+1):
          RandomizationNumber += 1
          SequenceNumber += 1
          writer.writerow({'Randomization number': RandomizationNumber, 'Treatment Code': TreatmentArm, 'Sequence Number': SequenceNumber, 'Cohort Code': Cohort})
