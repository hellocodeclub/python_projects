import xmltodict, json

obj = xmltodict.parse("""
<employees>
	<employee>
  		<name>Dave</name>
        <role>Sale Assistant</role>
        <age>34</age>
    </employee>
</employees>
""")

print(xmltodict.unparse(obj, pretty=True))
print(json.dumps(obj))
print(obj["employees"]["employee"]['name'])

with open('data.xml', 'r') as myfile:
    obj = xmltodict.parse(myfile.read())
print(json.dumps(obj))


# Converting from XML to python objects using untangle

import untangle
obj = untangle.parse('data.xml')
print(obj.employees.employee.name.cdata)

