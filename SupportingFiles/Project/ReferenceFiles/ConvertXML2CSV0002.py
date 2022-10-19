# https://python.plainenglish.io/converting-xml-to-csv-using-python-d723a3df3de1
# 1
import csv
import xmltodict

# 2
# Reading xml file
with open("sample.xml", 'r') as file:
    filedata = file.read()

# Converting xml to python dictionary (ordered dict)
data_dict = xmltodict.parse(filedata)

# 3
# creating a list of employee data
employee_data_list = [dict(x) for x in data_dict["employees"]["employee"]]

'''
<employees>
   <employee>
      <name>Carolina</name>
        <role>Data Engineer</role>
        <age>24</age>
    </employee>
    <employee>
      <name>Roosaka</name>
        <role>Data Scientist</role>
        <age>27</age>
    </employee>
    <employee>
      <name>Kumar</name>
        <role>Machine Learning Engineer</role>
        <age>31</age>
    </employee>
    <employee>
      <name>Vijay</name>
        <role>Devops Engineer</role>
        <age>26</age>
    </employee>
</employees>

'''
