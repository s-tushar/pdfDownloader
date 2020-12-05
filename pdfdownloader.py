import csv
from pathlib import Path
import requests
import shutil, os
import datetime 

#User Configurables
inputCsvPath='/home/tushar/Projects/pyselem/links.csv'
outputFolderPath = "/home/tushar/Projects/pdfDownloader"

#temp array
files=[]

#Create Directory with name=currentTime to save downloaded PDFs
current_time = datetime.datetime.now()
directory = str(current_time)
path = os.path.join(outputFolderPath, directory) 
os.mkdir(path) 

#Download PDFs 
with open(inputCsvPath, newline='') as Excel:
    reader = csv.reader(Excel)
    for row in reader:
        name= row[1]
        url = row[0]
        name=name+'.pdf'
        try:
            filename = Path(name)
            response = requests.get(url)
            filename.write_bytes(response.content)
            files.append(name)
            print("Dowloaded ", name)
        except:
            print("An Error occurred while ", name)

#Move downloaded PDFs to above created folder
for f in files:
    shutil.move(f, directory)