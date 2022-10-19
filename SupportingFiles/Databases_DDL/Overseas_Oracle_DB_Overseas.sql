DROP SEQUENCE seq_APPLICANT;
DROP TABLE APPLICANT CASCADE CONSTRAINTS;
DROP TABLE ASSESMENT CASCADE CONSTRAINTS;
DROP TABLE COLLEGES_APPLIED CASCADE CONSTRAINTS;
DROP TABLE DEPENDENTS CASCADE CONSTRAINTS;
DROP TABLE DOCUMENTS CASCADE CONSTRAINTS;
DROP TABLE EDUCATION CASCADE CONSTRAINTS;
DROP TABLE EMPLOYEE CASCADE CONSTRAINTS;
DROP TABLE ENROLLMENT CASCADE CONSTRAINTS;
DROP TABLE FRANCHISE CASCADE CONSTRAINTS;
DROP TABLE IDENTITIY CASCADE CONSTRAINTS;
DROP TABLE PAYMENTS CASCADE CONSTRAINTS;
DROP TABLE PROJECT_LOOKUP CASCADE CONSTRAINTS;
DROP TABLE WORK_EXPERIENCE CASCADE CONSTRAINTS;

CREATE SEQUENCE seq_APPLICANT;
CREATE TABLE APPLICANT (
  APPLICATION_ID        varchar2(15) NOT NULL, 
  Application_Date      date NOT NULL, 
  First_Name            varchar2(100) NOT NULL, 
  Last_Name             varchar2(100) NOT NULL, 
  Date_Of_Birth         date NOT NULL, 
  Gender                char(1) NOT NULL, 
  Nationality           varchar2(25) NOT NULL, 
  Father_Spouse_Name    varchar2(100) NOT NULL, 
  Mother_Name           varchar2(100) NOT NULL, 
  Marital_Status        varchar2(30) NOT NULL, 
  Mobile_No             number(10) NOT NULL, 
  EMail                 varchar2(100) NOT NULL, 
  Address               varchar2(1000) NOT NULL, 
  City                  varchar2(30) NOT NULL, 
  Village               varchar2(30), 
  Mandal                varchar2(30), 
  District              varchar2(30) NOT NULL, 
  State                 varchar2(30) NOT NULL, 
  Country               varchar2(30) NOT NULL, 
  PinCode               number(10) NOT NULL, 
  Photo                 blob NOT NULL, 
  Referred_By           varchar2(10) NOT NULL, 
  Application_Status    varchar2(10) NOT NULL, 
  Created_By            number(10), 
  Application_Source_ID number(10), 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE ASSESMENT (
  APPLICATION_ID    varchar2(15) NOT NULL, 
  ASSESSOR_ID       number(10) NOT NULL, 
  Assement_Date     date NOT NULL, 
  Assessment_Type   number(10) NOT NULL, 
  Status            varchar2(20) NOT NULL, 
  Document_ID       varchar2(30), 
  Image             blob NOT NULL, 
  Active            char(1) NOT NULL, 
  Comments          varchar2(1000) NOT NULL, 
  Assessor_Comments varchar2(1000) NOT NULL, 
  Assement_Type     number(10) NOT NULL, 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE COLLEGES_APPLIED (
  APPLICATION_ID     varchar2(15) NOT NULL, 
  Course_Applied     varchar2(100) NOT NULL, 
  Course_Group       varchar2(50) NOT NULL, 
  Course_Branch      varchar2(50) NOT NULL, 
  College_Applied    varchar2(100) NOT NULL, 
  Board_University   varchar2(100) NOT NULL, 
  Location           varchar2(200) NOT NULL, 
  Application_Status varchar2(20) NOT NULL, 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE DEPENDENTS (
  APPLICATION_ID       varchar2(15) NOT NULL, 
  Dependent_ID         varchar2(30) NOT NULL, 
  Dependent_Name       varchar2(100) NOT NULL, 
  RELATIONSHIP_TYPE_ID varchar2(20) NOT NULL, 
  Date_Of_Birth        date NOT NULL, 
  Country              number(10) NOT NULL, 
  Document_Image       blob NOT NULL, 
  Phone                number(15), 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE DOCUMENTS (
  DOCUMENT_SOURCE_ID           varchar2(15) NOT NULL, 
  Document_Source              varchar2(20) NOT NULL, 
  Document_File_Type           varchar2(50) NOT NULL, 
  Document_Uploaded_Date       timestamp(0) NOT NULL, 
  Document_File                blob NOT NULL, 
  Comments                     varchar2(1000) NOT NULL, 
  Document_Uploaded_By         varchar2(15), 
  Document_Verification_Status varchar2(15), 
  Document_Verified_By         number(10), 
  DOCUMENT_ID                  varchar2(20));
CREATE TABLE EDUCATION (
  APPLICATION_ID         varchar2(15) NOT NULL, 
  Course_Name            varchar2(100) NOT NULL, 
  Course_Group           varchar2(50) NOT NULL, 
  Course_Branch          varchar2(50) NOT NULL, 
  Course_Start_Date      date NOT NULL, 
  Course_Completion_Date date NOT NULL, 
  Percentage             number(5, 2) NOT NULL, 
  Institution            varchar2(100) NOT NULL, 
  Board_University       varchar2(100) NOT NULL, 
  Gap_Duration_Months    number(3), 
  Location               varchar2(200) NOT NULL, 
  DOCUMENT_ID            varchar2(20) NOT NULL, 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE EMPLOYEE (
  EMPLOYEE_ID  number(10) GENERATED AS IDENTITY, 
  FIRST_NAME   varchar2(30) NOT NULL, 
  LAST_NAME    varchar2(30) NOT NULL, 
  DATE_OF_JOIN date NOT NULL, 
  DEPARTMENT   varchar2(10) NOT NULL, 
  DESIGNATION  varchar2(100) NOT NULL, 
  PHONE_NO     number(15) NOT NULL, 
  EMAIL        varchar2(255) NOT NULL, 
  USER_ID      varchar2(10) NOT NULL, 
  PASSWORD     varchar2(10) NOT NULL, 
  LAST_LOGIN   timestamp(30) NOT NULL, 
  ACTIVE       varchar2(10) NOT NULL, 
  AADHAAR_NO   number(20) NOT NULL, 
  ADDRESS      number(255) NOT NULL, 
  PHOTO        blob NOT NULL, 
  SALARY       number(10, 2) NOT NULL, 
  PF_NO        varchar2(20) NOT NULL, 
  PAN_CARD     varchar2(10) NOT NULL, 
  BRANCH_CODE  varchar2(10) NOT NULL, 
  USER_TYPE    number(10) NOT NULL, 
  MANAGER_ID   number(10) NOT NULL, 
  PRIMARY KEY (EMPLOYEE_ID));
CREATE TABLE ENROLLMENT (
  APPLICATION_ID        varchar2(15) NOT NULL, 
  TRAINING_ID           varchar2(20) NOT NULL, 
  Training_Start_Date   date NOT NULL, 
  Training_End_Date     date NOT NULL, 
  Traning_Duration      number(10) NOT NULL, 
  Location              varchar2(200) NOT NULL, 
  Training_Status_ID    number(10) NOT NULL, 
  Training_Time_Breakup varchar2(10) NOT NULL, 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE FRANCHISE (
  FRANCHISE_ID         varchar2(15) NOT NULL, 
  FRANCHISE_NAME       varchar2(100) NOT NULL, 
  MANAGER_ID           number(10) NOT NULL, 
  FIRST_NAME           varchar2(30) NOT NULL, 
  LAST_NAME            varchar2(30) NOT NULL, 
  REGISTRATION_DATE    date NOT NULL, 
  PHONE_NO             number(15) NOT NULL, 
  ALTERNATE_CONTACT_NO number(10), 
  EMAIL                varchar2(255) NOT NULL, 
  DESIGNATION          varchar2(100) NOT NULL, 
  USER_ID              varchar2(10) NOT NULL, 
  PASSWORD             varchar2(10) NOT NULL, 
  LAST_LOGIN           timestamp(30) NOT NULL, 
  ACTIVE               number(10) NOT NULL, 
  AADHAAR_NO           number(20) NOT NULL, 
  ADDRESS              number(255) NOT NULL, 
  PHOTO                blob NOT NULL, 
  DOCUMENT_ID          number(10) NOT NULL, 
  COMMISSION_AMOUNT    number(10, 2) NOT NULL, 
  PAN_CARD             varchar2(10) NOT NULL, 
  GSTNO                varchar2(30) NOT NULL, 
  CITY                 number(10) NOT NULL, 
  STATE                number(10) NOT NULL, 
  COUNTRY              number(10) NOT NULL, 
  PINCODE              number(10) NOT NULL, 
  Comments             varchar2(1000) NOT NULL, 
  PRIMARY KEY (FRANCHISE_ID));
CREATE TABLE IDENTITIY (
  APPLICATION_ID      varchar2(15) NOT NULL, 
  Proof_Of_Identity   varchar2(20) NOT NULL, 
  ID_Number           varchar2(20) NOT NULL, 
  Issued_Organization varchar2(100) NOT NULL, 
  Start_Date          date NOT NULL, 
  End_Date            date NOT NULL, 
  Place_Of_ID_Issued  varchar2(100) NOT NULL, 
  Country             number(10) NOT NULL, 
  Document_Image      blob NOT NULL, 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE PAYMENTS (
  PAYMENT_DATE             date NOT NULL, 
  AMOUNT_PAID              number(12, 2) NOT NULL, 
  MODE_OF_PAYMENT          varchar2(20) NOT NULL, 
  MODE_OF_PAYMENT_NO       varchar2(30) NOT NULL, 
  PAYMENT_REFERENCE_NO     number(30) NOT NULL, 
  TRANSACTION_REFERENCE_NO varchar2(20) NOT NULL, 
  SGST                     number(10) DEFAULT 0 NOT NULL, 
  IGST                     number(10) DEFAULT 0 NOT NULL, 
  GSTNO                    varchar2(20) NOT NULL, 
  TRANSACTION_TYPE_ID      varchar2(20) NOT NULL, 
  APPLICATION_ID           varchar2(15) NOT NULL);
CREATE TABLE PROJECT_LOOKUP (
  LOOKUP_ID          varchar2(20) NOT NULL, 
  LOOKUP_CODE        varchar2(10) NOT NULL UNIQUE, 
  LOOKUP_TYPE        varchar2(10) NOT NULL UNIQUE, 
  LOOKUP_CATEGORY    varchar2(10) NOT NULL UNIQUE, 
  LOOKUP_NAME        varchar2(10) NOT NULL, 
  LOOKUP_DESCRIPTION varchar2(100) NOT NULL, 
  ACTIVE             char(1) NOT NULL, 
  PRIMARY KEY (LOOKUP_ID));
CREATE TABLE WORK_EXPERIENCE (
  APPLICATION_ID          varchar2(15) NOT NULL, 
  Company_Name            varchar2(100) NOT NULL, 
  INDUSTRY_CATEGORY_ID    varchar2(20) NOT NULL, 
  Designation             varchar2(50) NOT NULL, 
  Job_Description         varchar2(1000) NOT NULL, 
  Total_Experience_Months number(10) NOT NULL, 
  Start_Date              date NOT NULL, 
  End_Date                date NOT NULL, 
  Location                varchar2(100) NOT NULL, 
  Country                 number(30) DEFAULT INDIA NOT NULL, 
  PRIMARY KEY (APPLICATION_ID));
ALTER TABLE EDUCATION ADD CONSTRAINT FKEDUCATION728549 FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE WORK_EXPERIENCE ADD CONSTRAINT FKWORK_EXPER651023 FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE IDENTITIY ADD CONSTRAINT FKIDENTITIY838913 FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE DEPENDENTS ADD CONSTRAINT FKDEPENDENTS310083 FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE COLLEGES_APPLIED ADD CONSTRAINT FKCOLLEGES_A372576 FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE ASSESMENT ADD CONSTRAINT FKASSESMENT377718 FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE ENROLLMENT ADD CONSTRAINT FKENROLLMENT929476 FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE DOCUMENTS ADD CONSTRAINT FKDOCUMENTS918979 FOREIGN KEY (DOCUMENT_SOURCE_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE FRANCHISE ADD CONSTRAINT FKFRANCHISE376026 FOREIGN KEY (MANAGER_ID) REFERENCES EMPLOYEE (EMPLOYEE_ID);
ALTER TABLE ASSESMENT ADD CONSTRAINT FKASSESMENT456826 FOREIGN KEY (ASSESSOR_ID) REFERENCES EMPLOYEE (EMPLOYEE_ID);
ALTER TABLE DOCUMENTS ADD CONSTRAINT FKDOCUMENTS124652 FOREIGN KEY (DOCUMENT_SOURCE_ID) REFERENCES FRANCHISE (FRANCHISE_ID);
ALTER TABLE ENROLLMENT ADD CONSTRAINT FKENROLLMENT516985 FOREIGN KEY (TRAINING_ID) REFERENCES PROJECT_LOOKUP (LOOKUP_ID);
ALTER TABLE PAYMENTS ADD CONSTRAINT FKPAYMENTS939366 FOREIGN KEY (TRANSACTION_TYPE_ID) REFERENCES PROJECT_LOOKUP (LOOKUP_ID);
ALTER TABLE COLLEGES_APPLIED ADD CONSTRAINT FKCOLLEGES_A317257 FOREIGN KEY (Application_Status) REFERENCES PROJECT_LOOKUP (LOOKUP_ID);
ALTER TABLE IDENTITIY ADD CONSTRAINT FKIDENTITIY475486 FOREIGN KEY (Proof_Of_Identity) REFERENCES PROJECT_LOOKUP (LOOKUP_ID);
ALTER TABLE DEPENDENTS ADD CONSTRAINT FKDEPENDENTS908754 FOREIGN KEY (RELATIONSHIP_TYPE_ID) REFERENCES PROJECT_LOOKUP (LOOKUP_ID);
ALTER TABLE WORK_EXPERIENCE ADD CONSTRAINT FKWORK_EXPER301826 FOREIGN KEY (INDUSTRY_CATEGORY_ID) REFERENCES PROJECT_LOOKUP (LOOKUP_ID);
ALTER TABLE PAYMENTS ADD CONSTRAINT FKPAYMENTS199360 FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE ASSESMENT ADD CONSTRAINT FKASSESMENT377719 FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);

SELECT APPLICATION_ID, Application_Date, First_Name, Last_Name, Date_Of_Birth, Gender, Nationality, Father_Spouse_Name, Mother_Name, Marital_Status, Mobile_No, EMail, Address, City, Village, Mandal, District, State, Country, PinCode, Photo, Referred_By, Application_Status, Created_By, Application_Source_ID 
  FROM APPLICANT;
SELECT APPLICATION_ID, ASSESSOR_ID, Assement_Date, Assessment_Type, Status, Document_ID, Image, Active, Comments, Assessor_Comments, Assement_Type 
  FROM ASSESMENT;
SELECT APPLICATION_ID, Course_Applied, Course_Group, Course_Branch, College_Applied, Board_University, Location, Application_Status 
  FROM COLLEGES_APPLIED;
SELECT APPLICATION_ID, Dependent_ID, Dependent_Name, RELATIONSHIP_TYPE_ID, Date_Of_Birth, Country, Document_Image, Phone 
  FROM DEPENDENTS;
SELECT DOCUMENT_SOURCE_ID, Document_Source, Document_File_Type, Document_Uploaded_Date, Document_File, Comments, Document_Uploaded_By, Document_Verification_Status, Document_Verified_By, DOCUMENT_ID 
  FROM DOCUMENTS;
SELECT APPLICATION_ID, Course_Name, Course_Group, Course_Branch, Course_Start_Date, Course_Completion_Date, Percentage, Institution, Board_University, Gap_Duration_Months, Location, DOCUMENT_ID 
  FROM EDUCATION;
SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, DATE_OF_JOIN, DEPARTMENT, DESIGNATION, PHONE_NO, EMAIL, USER_ID, PASSWORD, LAST_LOGIN, ACTIVE, AADHAAR_NO, ADDRESS, PHOTO, SALARY, PF_NO, PAN_CARD, BRANCH_CODE, USER_TYPE, MANAGER_ID 
  FROM EMPLOYEE;
SELECT APPLICATION_ID, TRAINING_ID, Training_Start_Date, Training_End_Date, Traning_Duration, Location, Training_Status_ID, Training_Time_Breakup 
  FROM ENROLLMENT;
SELECT FRANCHISE_ID, FRANCHISE_NAME, MANAGER_ID, FIRST_NAME, LAST_NAME, REGISTRATION_DATE, PHONE_NO, ALTERNATE_CONTACT_NO, EMAIL, DESIGNATION, USER_ID, PASSWORD, LAST_LOGIN, ACTIVE, AADHAAR_NO, ADDRESS, PHOTO, DOCUMENT_ID, COMMISSION_AMOUNT, PAN_CARD, GSTNO, CITY, STATE, COUNTRY, PINCODE, Comments 
  FROM FRANCHISE;
SELECT APPLICATION_ID, Proof_Of_Identity, ID_Number, Issued_Organization, Start_Date, End_Date, Place_Of_ID_Issued, Country, Document_Image 
  FROM IDENTITIY;
SELECT PAYMENT_DATE, AMOUNT_PAID, MODE_OF_PAYMENT, MODE_OF_PAYMENT_NO, PAYMENT_REFERENCE_NO, TRANSACTION_REFERENCE_NO, SGST, IGST, GSTNO, TRANSACTION_TYPE_ID, APPLICATION_ID 
  FROM PAYMENTS;
SELECT LOOKUP_ID, LOOKUP_CODE, LOOKUP_TYPE, LOOKUP_CATEGORY, LOOKUP_NAME, LOOKUP_DESCRIPTION, ACTIVE 
  FROM PROJECT_LOOKUP;
SELECT APPLICATION_ID, Company_Name, INDUSTRY_CATEGORY_ID, Designation, Job_Description, Total_Experience_Months, Start_Date, End_Date, Location, Country 
  FROM WORK_EXPERIENCE;

INSERT INTO APPLICANT
  (APPLICATION_ID, 
  Application_Date, 
  First_Name, 
  Last_Name, 
  Date_Of_Birth, 
  Gender, 
  Nationality, 
  Father_Spouse_Name, 
  Mother_Name, 
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
  Application_Source_ID) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO ASSESMENT
  (APPLICATION_ID, 
  ASSESSOR_ID, 
  Assement_Date, 
  Assessment_Type, 
  Status, 
  Document_ID, 
  Image, 
  Active, 
  Comments, 
  Assessor_Comments, 
  Assement_Type) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO COLLEGES_APPLIED
  (APPLICATION_ID, 
  Course_Applied, 
  Course_Group, 
  Course_Branch, 
  College_Applied, 
  Board_University, 
  Location, 
  Application_Status) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO DEPENDENTS
  (APPLICATION_ID, 
  Dependent_ID, 
  Dependent_Name, 
  RELATIONSHIP_TYPE_ID, 
  Date_Of_Birth, 
  Country, 
  Document_Image, 
  Phone) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO DOCUMENTS
  (DOCUMENT_SOURCE_ID, 
  Document_Source, 
  Document_File_Type, 
  Document_Uploaded_Date, 
  Document_File, 
  Comments, 
  Document_Uploaded_By, 
  Document_Verification_Status, 
  Document_Verified_By, 
  DOCUMENT_ID) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO EDUCATION
  (APPLICATION_ID, 
  Course_Name, 
  Course_Group, 
  Course_Branch, 
  Course_Start_Date, 
  Course_Completion_Date, 
  Percentage, 
  Institution, 
  Board_University, 
  Gap_Duration_Months, 
  Location, 
  DOCUMENT_ID) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO EMPLOYEE
  (EMPLOYEE_ID, 
  FIRST_NAME, 
  LAST_NAME, 
  DATE_OF_JOIN, 
  DEPARTMENT, 
  DESIGNATION, 
  PHONE_NO, 
  EMAIL, 
  USER_ID, 
  PASSWORD, 
  LAST_LOGIN, 
  ACTIVE, 
  AADHAAR_NO, 
  ADDRESS, 
  PHOTO, 
  SALARY, 
  PF_NO, 
  PAN_CARD, 
  BRANCH_CODE, 
  USER_TYPE, 
  MANAGER_ID) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO ENROLLMENT
  (APPLICATION_ID, 
  TRAINING_ID, 
  Training_Start_Date, 
  Training_End_Date, 
  Traning_Duration, 
  Location, 
  Training_Status_ID, 
  Training_Time_Breakup) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO FRANCHISE
  (FRANCHISE_ID, 
  FRANCHISE_NAME, 
  MANAGER_ID, 
  FIRST_NAME, 
  LAST_NAME, 
  REGISTRATION_DATE, 
  PHONE_NO, 
  ALTERNATE_CONTACT_NO, 
  EMAIL, 
  DESIGNATION, 
  USER_ID, 
  PASSWORD, 
  LAST_LOGIN, 
  ACTIVE, 
  AADHAAR_NO, 
  ADDRESS, 
  PHOTO, 
  DOCUMENT_ID, 
  COMMISSION_AMOUNT, 
  PAN_CARD, 
  GSTNO, 
  CITY, 
  STATE, 
  COUNTRY, 
  PINCODE, 
  Comments) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO IDENTITIY
  (APPLICATION_ID, 
  Proof_Of_Identity, 
  ID_Number, 
  Issued_Organization, 
  Start_Date, 
  End_Date, 
  Place_Of_ID_Issued, 
  Country, 
  Document_Image) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO PAYMENTS
  (PAYMENT_DATE, 
  AMOUNT_PAID, 
  MODE_OF_PAYMENT, 
  MODE_OF_PAYMENT_NO, 
  PAYMENT_REFERENCE_NO, 
  TRANSACTION_REFERENCE_NO, 
  SGST, 
  IGST, 
  GSTNO, 
  TRANSACTION_TYPE_ID, 
  APPLICATION_ID) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO PROJECT_LOOKUP
  (LOOKUP_ID, 
  LOOKUP_CODE, 
  LOOKUP_TYPE, 
  LOOKUP_CATEGORY, 
  LOOKUP_NAME, 
  LOOKUP_DESCRIPTION, 
  ACTIVE) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO WORK_EXPERIENCE
  (APPLICATION_ID, 
  Company_Name, 
  INDUSTRY_CATEGORY_ID, 
  Designation, 
  Job_Description, 
  Total_Experience_Months, 
  Start_Date, 
  End_Date, 
  Location, 
  Country) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);

UPDATE APPLICANT SET 
  Application_Date = ?, 
  First_Name = ?, 
  Last_Name = ?, 
  Date_Of_Birth = ?, 
  Gender = ?, 
  Nationality = ?, 
  Father_Spouse_Name = ?, 
  Mother_Name = ?, 
  Marital_Status = ?, 
  Mobile_No = ?, 
  EMail = ?, 
  Address = ?, 
  City = ?, 
  Village = ?, 
  Mandal = ?, 
  District = ?, 
  State = ?, 
  Country = ?, 
  PinCode = ?, 
  Photo = ?, 
  Referred_By = ?, 
  Application_Status = ?, 
  Created_By = ?, 
  Application_Source_ID = ? 
WHERE
  APPLICATION_ID = ?;
UPDATE ASSESMENT SET 
  ASSESSOR_ID = ?, 
  Assement_Date = ?, 
  Assessment_Type = ?, 
  Status = ?, 
  Document_ID = ?, 
  Image = ?, 
  Active = ?, 
  Comments = ?, 
  Assessor_Comments = ?, 
  Assement_Type = ? 
WHERE
  APPLICATION_ID = ?;
UPDATE COLLEGES_APPLIED SET 
  Course_Applied = ?, 
  Course_Group = ?, 
  Course_Branch = ?, 
  College_Applied = ?, 
  Board_University = ?, 
  Location = ?, 
  Application_Status = ? 
WHERE
  APPLICATION_ID = ?;
UPDATE DEPENDENTS SET 
  Dependent_ID = ?, 
  Dependent_Name = ?, 
  RELATIONSHIP_TYPE_ID = ?, 
  Date_Of_Birth = ?, 
  Country = ?, 
  Document_Image = ?, 
  Phone = ? 
WHERE
  APPLICATION_ID = ?;
UPDATE DOCUMENTS SET 
  DOCUMENT_SOURCE_ID = ?, 
  Document_Source = ?, 
  Document_File_Type = ?, 
  Document_Uploaded_Date = ?, 
  Document_File = ?, 
  Comments = ?, 
  Document_Uploaded_By = ?, 
  Document_Verification_Status = ?, 
  Document_Verified_By = ?, 
  DOCUMENT_ID = ? 
WHERE
  ;
UPDATE EDUCATION SET 
  Course_Name = ?, 
  Course_Group = ?, 
  Course_Branch = ?, 
  Course_Start_Date = ?, 
  Course_Completion_Date = ?, 
  Percentage = ?, 
  Institution = ?, 
  Board_University = ?, 
  Gap_Duration_Months = ?, 
  Location = ?, 
  DOCUMENT_ID = ? 
WHERE
  APPLICATION_ID = ?;
UPDATE EMPLOYEE SET 
  FIRST_NAME = ?, 
  LAST_NAME = ?, 
  DATE_OF_JOIN = ?, 
  DEPARTMENT = ?, 
  DESIGNATION = ?, 
  PHONE_NO = ?, 
  EMAIL = ?, 
  USER_ID = ?, 
  PASSWORD = ?, 
  LAST_LOGIN = ?, 
  ACTIVE = ?, 
  AADHAAR_NO = ?, 
  ADDRESS = ?, 
  PHOTO = ?, 
  SALARY = ?, 
  PF_NO = ?, 
  PAN_CARD = ?, 
  BRANCH_CODE = ?, 
  USER_TYPE = ?, 
  MANAGER_ID = ? 
WHERE
  EMPLOYEE_ID = ?;
UPDATE ENROLLMENT SET 
  TRAINING_ID = ?, 
  Training_Start_Date = ?, 
  Training_End_Date = ?, 
  Traning_Duration = ?, 
  Location = ?, 
  Training_Status_ID = ?, 
  Training_Time_Breakup = ? 
WHERE
  APPLICATION_ID = ?;
UPDATE FRANCHISE SET 
  FRANCHISE_NAME = ?, 
  MANAGER_ID = ?, 
  FIRST_NAME = ?, 
  LAST_NAME = ?, 
  REGISTRATION_DATE = ?, 
  PHONE_NO = ?, 
  ALTERNATE_CONTACT_NO = ?, 
  EMAIL = ?, 
  DESIGNATION = ?, 
  USER_ID = ?, 
  PASSWORD = ?, 
  LAST_LOGIN = ?, 
  ACTIVE = ?, 
  AADHAAR_NO = ?, 
  ADDRESS = ?, 
  PHOTO = ?, 
  DOCUMENT_ID = ?, 
  COMMISSION_AMOUNT = ?, 
  PAN_CARD = ?, 
  GSTNO = ?, 
  CITY = ?, 
  STATE = ?, 
  COUNTRY = ?, 
  PINCODE = ?, 
  Comments = ? 
WHERE
  FRANCHISE_ID = ?;
UPDATE IDENTITIY SET 
  Proof_Of_Identity = ?, 
  ID_Number = ?, 
  Issued_Organization = ?, 
  Start_Date = ?, 
  End_Date = ?, 
  Place_Of_ID_Issued = ?, 
  Country = ?, 
  Document_Image = ? 
WHERE
  APPLICATION_ID = ?;
UPDATE PAYMENTS SET 
  PAYMENT_DATE = ?, 
  AMOUNT_PAID = ?, 
  MODE_OF_PAYMENT = ?, 
  MODE_OF_PAYMENT_NO = ?, 
  PAYMENT_REFERENCE_NO = ?, 
  TRANSACTION_REFERENCE_NO = ?, 
  SGST = ?, 
  IGST = ?, 
  GSTNO = ?, 
  TRANSACTION_TYPE_ID = ?, 
  APPLICATION_ID = ? 
WHERE
  ;
UPDATE PROJECT_LOOKUP SET 
  LOOKUP_CODE = ?, 
  LOOKUP_TYPE = ?, 
  LOOKUP_CATEGORY = ?, 
  LOOKUP_NAME = ?, 
  LOOKUP_DESCRIPTION = ?, 
  ACTIVE = ? 
WHERE
  LOOKUP_ID = ?;
UPDATE WORK_EXPERIENCE SET 
  Company_Name = ?, 
  INDUSTRY_CATEGORY_ID = ?, 
  Designation = ?, 
  Job_Description = ?, 
  Total_Experience_Months = ?, 
  Start_Date = ?, 
  End_Date = ?, 
  Location = ?, 
  Country = ? 
WHERE
  APPLICATION_ID = ?;

DELETE FROM APPLICANT 
  WHERE APPLICATION_ID = ?;
DELETE FROM ASSESMENT 
  WHERE APPLICATION_ID = ?;
DELETE FROM COLLEGES_APPLIED 
  WHERE APPLICATION_ID = ?;
DELETE FROM DEPENDENTS 
  WHERE APPLICATION_ID = ?;
DELETE FROM DOCUMENTS 
  WHERE ;
DELETE FROM EDUCATION 
  WHERE APPLICATION_ID = ?;
DELETE FROM EMPLOYEE 
  WHERE EMPLOYEE_ID = ?;
DELETE FROM ENROLLMENT 
  WHERE APPLICATION_ID = ?;
DELETE FROM FRANCHISE 
  WHERE FRANCHISE_ID = ?;
DELETE FROM IDENTITIY 
  WHERE APPLICATION_ID = ?;
DELETE FROM PAYMENTS 
  WHERE ;
DELETE FROM PROJECT_LOOKUP 
  WHERE LOOKUP_ID = ?;
DELETE FROM WORK_EXPERIENCE 
  WHERE APPLICATION_ID = ?;
