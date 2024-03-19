from xml.etree import ElementTree
import csv

#Parse
xml = ElementTree.parse("data.xml")

#Create CSV
csvFile = open("data.csv", "w", encoding="utf-8")
csvFileWriter = csv.writer(csvFile)

#ADD HEADER
csvFileWriter.writerow(["name", "role", "age"])

for employee in xml.findall("employee"):
    if(employee):
        name = employee.find("name")
        role = employee.find("role")
        age = employee.find("age")

        csvLine = [name.text, role.text, age.text]
        csvFileWriter.writerow(csvLine)
csvFile.close()
