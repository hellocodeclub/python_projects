import xmltodict, csv
import time
starttime = time.time_ns()/1000000

# PARSE XML FILE
with open("data.xml") as xmlfile:
    xml = xmltodict.parse(xmlfile.read())

# CREATE CSV FILE
csvfile = open("data2.csv",'w',encoding='utf-8')
csvfile_writer = csv.writer(csvfile)

# ADD HEADER
csvfile_writer.writerow(["name","role","age"])

#FOR EACH EMPLOYEE
for employee in xml["employees"]["employee"]:

    # EXTRACT EMPLOYEE DETAILS
    csv_line = [employee["name"], employee["role"],employee["age"]]

    # ADD A NEW ROW TO CSV FILE
    csvfile_writer.writerow(csv_line)

endtime = time.time_ns()/1000000
delta = endtime - starttime
print(delta)

# first approach using built-in libraries, which means you don
# if 't need to install any extra library:



