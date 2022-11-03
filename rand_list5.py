# https://docs.python.org/3/library/csv.html
import random, os, csv
from csv import DictWriter

def threes(value):
  last_digit = int(repr(value)[-1])
  if last_digit % 3 == 0:
    return "3"
  elif last_digit % 2 == 0:
    return "2"
  else:
    return "1"


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
RandListImportFile = os.path.join(desktop, 'RandList.csv')

with open(RandListImportFile, 'w', newline='') as csvfile:
    fieldnames = ['Randomization number', 'Treatment Code', 'Stratum Code', 'Sequence Number', 'Block Number', 'Cohort Code']
    writer: DictWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    n: int
    BlockSize = 4
    NumberOfBlocks = 50
    NumberOfRecords = BlockSize * NumberOfBlocks
    BlockNumber = 1
    SequenceNumber = 2000
    RandomizationNumber = 11000
    BlockNumber = 1000
    RandList = []

    for n in range(1, NumberOfRecords+1):
      RandList.append(RandomizationNumber + n)

    random.shuffle(RandList)

    for n in range(1, NumberOfBlocks+1):
        BlockNumber += 1
        if BlockNumber % 2 == 0:
            TreatmentArm = "TA2"
            StratumCode = "02"
            Cohort = "Cohort 2"
        else:
            TreatmentArm = "TA1"
            StratumCode = "01"
            Cohort = "Cohort 1"
        for j in range(1, BlockSize+1):
          RandomizationNumber = RandList.pop(0)
          SequenceNumber += 1
          writer.writerow({'Randomization number': RandomizationNumber, 'Treatment Code': TreatmentArm, 'Stratum Code': StratumCode, 'Sequence Number': SequenceNumber, 'Block Number': BlockNumber, 'Cohort Code': Cohort})
