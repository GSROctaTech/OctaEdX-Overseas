from faker import Faker
import numpy as np
import pandas as pd

industry = ['Automotive', 'Health Care', 'Manufacturing', 'High Tech', 'Retail']

fake = Faker()


def create_data(x):
    # dictionary
    b_user = {}
    for i in range(0, x):
        b_user[i] = {}
        b_user[i]['name'] = fake.name()
        b_user[i]['job'] = fake.job()
        b_user[i]['birthdate'] = fake.date_of_birth(minimum_age=18, maximum_age=65)
        b_user[i]['email'] = fake.company_email()
        b_user[i]['company'] = fake.company()
        b_user[i]['industry'] = fake.random_element(industry)
        b_user[i]['city'] = fake.city()
        b_user[i]['state'] = fake.state()
        b_user[i]['zipcode'] = fake.postcode()
        b_user[i]['netNew'] = fake.boolean(chance_of_getting_true=65)
        b_user[i]['sales_rounded'] = round(np.random.normal(1000, 200))
        b_user[i]['sales_decimal'] = np.random.normal(1000, 200)
        b_user[i]['priority'] = fake.random_digit()
        b_user[i]['industry2'] = np.random.choice(industry)

    return b_user


df = pd.DataFrame(create_data(5)).transpose()
print(df)
print(df.head(5))