import pandas_read_xml as pdx
df = pdx.read_xml("data.xml")
print(df.to_json())