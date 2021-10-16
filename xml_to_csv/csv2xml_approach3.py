import untangle, csv
import time
starttime = time.time_ns()/1000000

# PARSE XML FILE
xml = untangle.parse("data.xml")

# CREATE CSV FILE
csvfile = open("data3.csv",'w',encoding='utf-8')
csvfile_writer = csv.writer(csvfile)

# ADD HEADER
csvfile_writer.writerow(["name","role","age"])

# FOR EACH EMPLOYEE
for employee in xml.employees.employee:

    # EXTRACT EMPLOYEE DETAILS
    csv_line = [employee.name.cdata, employee.role.cdata, employee.age.cdata]

    # ADD NEW ROW TO CSV FILE
    csvfile_writer.writerow(csv_line)

endtime = time.time_ns()/1000000
delta = endtime - starttime
print(delta)
