from bs4 import BeautifulSoup
html_file = open('./sample.html')
html_parser = BeautifulSoup(html_file, 'html.parser')

li_elements = html_parser.select('.alert-primary')
print(len(li_elements))

heading_elements = html_parser.select('#heading-1')
print(len(heading_elements))

heading_element1 = html_parser.find(id='heading-1')
print(len(heading_element1))
print(type(heading_element1))

heading_element2 = html_parser.find_all(id='heading-1')
print(len(heading_element2))
print(type(heading_element2))

elements1= html_parser.find_all(id='heading-1') # by id
elements2 = html_parser.find_all('li')
print(elements2[0].text)
print(elements1[0].get_text())
print(len(elements2))
print(type(elements1))
print(type(elements2))
