import xml.etree.ElementTree as ET
data = '''<person>
<name>Jess</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
# find the name and email tag and print the text
print('Name:', tree.find('name').text)
# print the attribute of mail
print('Attr:', tree.find('email').get('hide'))
