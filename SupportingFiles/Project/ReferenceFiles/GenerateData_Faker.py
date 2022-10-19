# https://towardsdatascience.com/faker-library-in-python-an-intriguing-expedient-for-data-scientists-7dd06f953050

from faker import Faker
fakeobject = Faker()

fakeobject.name()
print(fakeobject.first_name())
print(fakeobject.last_name())
print(fakeobject.address())
print(fakeobject.job())
print(fakeobject.city())
print(fakeobject.latitude(), fakeobject.longitude())
print(fakeobject.text())

#This statement generates a dummy word
print(f'single word: {fakeobject.word()}')
#This statement genetaes a list of 5 dummy words
print(f'list of 5 words: {fakeobject.words(5)}')

listofwords = ['laptop', 'technology', 'science', 'mathematics', 'space']
print(f'random unique words: {fakeobject.words(3, listofwords, True)}')

# Generate Random Numbers
print(f'Random int: {fakeobject.random_int()}')
print(f'Random int: {fakeobject.random_int(0, 10)}')
print(f'Random digit: {fakeobject.random_digit()}')

# Generate Dates
print("Faker methods related to Date and Time")
print(f'Date of birth: {fakeobject.date_of_birth()}')
print(f'Year: {fakeobject.year()}')
print(f'Month: {fakeobject.month()}')
print(f'Month name: {fakeobject.month_name()}')
print(f'Day of week: {fakeobject.day_of_week()}')
print(f'Day of month: {fakeobject.day_of_month()}')
print(f'Time zone: {fakeobject.timezone()}')

# Generate Profile
profile1 = fakeobject.simple_profile()
profile2 = fakeobject.simple_profile('M')
profile3 = fakeobject.profile(sex='F')
print(profile1)
print(profile2)
print(profile3)

names = [fakeobject.unique.name() for i in range(10)]
for i in range (0,len(names)):
  print(names[i])


# Generate Seed Data
Faker.seed(10)
print(fakeobject.name())

print(fakeobject.name())

Faker.seed(10)
print(fakeobject.name())

# Generate Currency
print(f'currency: {fakeobject.currency()}')
print(f'currency name: {fakeobject.currency_name()}')
print(f'currency code: {fakeobject.currency_code()}')

# Generate Cryptocurrencies
print(f'currency name: {fakeobject.cryptocurrency_name()}')
print(f'currency code: {fakeobject.cryptocurrency()}')

# Generate Hash
print(f'sha256: {fakeobject.sha256()}')
print(f'md5: {fakeobject.md5()}')

# Generating Internet-related data
# Faker also provides methods for generating dummy data related to the internet such as email address,
# domain information, Internet protocol information, etc.

print("Domain related information")
print(f'Host name: {fakeobject.hostname()}')
print(f'Domain name: {fakeobject.domain_name()}')
print(f'Domain word: {fakeobject.domain_word()}')
print(f'TLD: {fakeobject.tld()}')
print(f'URL: {fakeobject.url()}')
print("")
print("Email related information")
print(f'Email: {fakeobject.email()}')
print(f'Safe email: {fakeobject.safe_email()}')
print(f'Free email: {fakeobject.free_email()}')
print(f'Company email: {fakeobject.company_email()}')
print("")
print("Internet protocol related information")
print(f'IPv4: {fakeobject.ipv4()}')
print(f'IPv6: {fakeobject.ipv6()}')
print(f'MAC address: {fakeobject.mac_address()}')


# Generate Language Data
# from faker import Faker
fakeobject = Faker('ja_JP') # Japan Language
for i in range(1,6):
    print(i," ",fakeobject.name())

# from faker import Faker
fake = Faker('hi_IN') # Hindi Language
for _ in range(10):
    print(fake.name())


# Generate Full Data
# from faker import Faker
# import pandas as pd
fakeobject = Faker()
person_data = [fakeobject.profile() for i in range(5)]
dataframe = pd.DataFrame(person_data)
dataframe

# Generate Large Data Set

#from faker import Faker
#import pandas as pd
fake = Faker()
profileData = [fake.profile() for i in range(100)]
df = pd.DataFrame(profileData)
df

# Generate Required Number of Dataset Rows
# from random import randint
# import pandas as pd

fake = Faker()

def input_data(x):
    # pandas dataframe
    data = pd.DataFrame()
    for i in range(0, x):
        data.loc[i, 'id'] = randint(1, 100)
        data.loc[i, 'name'] = fake.name()
        data.loc[i, 'address'] = fake.address()
        data.loc[i, 'latitude'] = str(fake.latitude())
        data.loc[i, 'longitude'] = str(fake.longitude())
    return data

input_data(10)

