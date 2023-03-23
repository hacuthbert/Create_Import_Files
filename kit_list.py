# https://docs.python.org/3/library/csv.html
#Set the starting kit and sequence numbers to the highest imported values.
#SELECT Max([Spec_Number]) StartingKitNumber
#      ,Max([Spec_SequenceNumber]) StartingSeqNumber
#  FROM [Fulfillment].[NumberedKit]
import csv
from csv import DictWriter

with open('KitList.csv', 'w', newline='') as csvfile:
    fieldnames = ['Kit Number', 'Kit Type', 'Sequence Number']
    writer: DictWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    n: int
    NumberOfRecords = 10
    StartingNumber = 3000
    StartingSequence = 4000
    Kit_Type = 'A'
    for n in range(1, NumberOfRecords+1):
        writer.writerow({'Kit Number': n+StartingNumber, 'Kit Type': Kit_Type, 'Sequence Number': n+StartingSequence})

