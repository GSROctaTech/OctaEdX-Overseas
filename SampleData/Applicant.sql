https://www.datacamp.com/tutorial/creating-synthetic-data-with-python-faker-tutorial
https://www.analyticsvidhya.com/blog/2021/09/how-to-create-dummy-data-in-python-using-faker-package/
https://faker.readthedocs.io/en/master/locales/en_IN.html
https://faker.readthedocs.io/en/master/locales.html
https://pypi.org/project/Faker/0.7.4/
https://fauxfactory.readthedocs.io/en/latest/#
https://blogs.sap.com/2021/05/26/generate-custom-datasets-using-python-faker/
https://towardsdatascience.com/generation-of-large-csv-data-using-python-faker-8cfcbedca7a7
https://github.com/Krishna-Parekh/pythonFaker
https://medium.com/@krishnaparekh_84257

INSERT INTO octaedx.APPLICANT
  (APPLICATION_ID, Application_Date, First_Name, Last_Name, Date_Of_Birth, Gender, Nationality, Father_Spouse_Name, Mother_Name, 
  Marital_Status, 
  Mobile_No, 
  EMail, 
  Address, 
  City, 
  Village, 
  Mandal, 
  District, 
  State, 
  Country, 
  PinCode, 
  Photo, 
  Referred_By, 
  Application_Status, 
  Created_By, 
  Application_Source_ID,
  Application_Submission_Status) 
VALUES 
  ('APPOEHYD0000001', 
  '10-10-2020', 
  'Applicant First Name', 
  'Applicant Last Name', 
  '10-12-1980', 
  'Male', 
  'Indian', 
  'Applicant Father Spouse Name', 
  'Applican Mother Name', 
  'Un Married', 
  9875674562, 
  'applicant@somedomain.com', 
  'Applicant Address', 
  'Applicant City', 
  'Applicant Village', 
  'Applicant Mandal', 
  'Applicant District', 
  'Applicant State', 
  'Applicant Country', 
  500001, 
  null, 
  'OCTAEDX', 
  'OPEN', 
  14678, 
  86876,
  'OPEN');