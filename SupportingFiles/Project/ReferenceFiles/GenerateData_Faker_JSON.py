'''
Generating JSON data

Faker also provides functionality to generate objects as per JSON format. It is possible to store the data
by generating a separate file. The following code snippet generates the details of 2 random employees
consisting of their Employee Id, Name, Address, Job, and City and finally generates a separate JSON file
that can be consumed anywhere else.
'''

#Import libraries
from faker import Faker
import json
from random import randint
#Initilaiize the object
fakeobject = Faker()
#Method to generate dummy details of the employees
def input_data(x):
    employee_data ={}
    for i in range(0, x):
      employee_data[i]={}
      employee_data[i]['Employee Id']= randint(1, 10)
      employee_data[i]['name']= fakeobject.name()
      employee_data[i]['address']= fakeobject.address()
      employee_data[i]['job']= fakeobject.job()
      employee_data[i]['city']= fakeobject.city()
      print(employee_data)
    #dictionary dumped as json in a json file
    with open('../employee.json', 'w') as fp:
      json.dump(employee_data, fp)
#defining the main method
def main():
    #variable to assign the number of employees
    number_of_employees = 2
    input_data(number_of_employees)
#Invoking the main method
main()