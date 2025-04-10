"""
Set the starting kit and sequence numbers to the highest imported values.
SELECT Max([Spec_Number]) StartingKitNumber
      ,Max([Spec_SequenceNumber]) StartingSeqNumber
  FROM [Fulfillment].[NumberedKit]
"""
import csv, os, shutil, random
from csv import DictWriter

with open('KitList.csv', 'w', newline='') as csvfile:
    fieldnames = ['Kit Number', 'Sequence Number', 'Kit Type']
    writer: DictWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    n: int
    NumberOfRecords = 1000
    StartingNumber = 13000
    StartingSequence = 4000
    Kit_Type = 'D'
    
    KitNumbers = []

    for n in range(1, NumberOfRecords+1):
      KitNumbers.append(StartingNumber + n)

    random.shuffle(KitNumbers)
    
    for n in range(1, NumberOfRecords+1):
        KitNumber = KitNumbers.pop(0)
        writer.writerow({'Kit Number': KitNumber, 'Sequence Number': n+StartingSequence, 'Kit Type': Kit_Type})

FirstKit = 1+StartingNumber
LastKit = n+StartingNumber
KitListName = f'KitListImport - kit type {Kit_Type} - {FirstKit}to{LastKit}.csv'

#https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python
os.rename('KitList.csv',KitListName)

#https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
myfile = os.path.join(desktop, KitListName)
shutil.move(KitListName, myfile)