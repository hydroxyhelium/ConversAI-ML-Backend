import pathlib
import sys
import csv 

datapath = "/Users/priyanshusharma/Downloads/package/messages" # refers to the directory where the discord data is saved
output_file = 'output.txt'


## a method made to recurse inside each folder and extract csv file 
def handle_file(file):
    contents = ""
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        
        line_count=0 
        for row in csv_reader:
            if line_count==0:
                pass
            else:
                if(contents!=""):
                    contents += "\n"
                contents += row[2]
            line_count += 1
    
    with open(output_file, 'a') as f:
        f.write(contents)


if(len(sys.argv)>2):
    datapath = sys.argv[1]

desktop = pathlib.Path(datapath)

file_generator = desktop.rglob("*.csv")

for file in file_generator:
    handle_file(file)


