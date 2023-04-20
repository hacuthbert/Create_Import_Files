# https://docs.python.org/3/library/csv.html
#Set the starting kit and sequence numbers to the highest imported values.
#SELECT Max([Spec_Number]) StartingKitNumber
#      ,Max([Spec_SequenceNumber]) StartingSeqNumber
#  FROM [Fulfillment].[NumberedKit]
import csv, os, shutil
from csv import DictWriter

with open('KitList.csv', 'w', newline='') as csvfile:
    fieldnames = ['Kit Number', 'Kit Type', 'Sequence Number']
    writer: DictWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    n: int
    NumberOfRecords = 400000
    StartingNumber = 700000
    StartingSequence = 700000
    Kit_Type = 'B'
    for n in range(1, NumberOfRecords+1):
        writer.writerow({'Kit Number': n+StartingNumber, 'Kit Type': Kit_Type, 'Sequence Number': n+StartingSequence})

FirstKit = 1+StartingNumber
LastKit = n+StartingNumber
KitListName = f'KitListImport - kit type {Kit_Type} - {FirstKit}to{LastKit}.csv'

#https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python
os.rename('KitList.csv',KitListName)

#https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
myfile = os.path.join(desktop, KitListName)
shutil.move(KitListName, myfile)