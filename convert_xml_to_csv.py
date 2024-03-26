from xml.etree import ElementTree
import csv

#Parse
xml = ElementTree.parse("bank.xml")

#Create CSV
csvFile = open("bank.csv", "w", encoding="utf-8")
csvFileWriter = csv.writer(csvFile)

#ADD HEADER
csvFileWriter.writerow(["name", "country", "age"])

for customer in xml.findall("customer"):
    if(customer):
        name = customer.find("name")
        country = customer.find("country")
        age = customer.find("age")

        csvLine = [name.text, country.text, age.text]
        csvFileWriter.writerow(csvLine)
csvFile.close()
