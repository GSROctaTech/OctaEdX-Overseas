DROP TABLE IF EXISTS APPLICANT;
DROP TABLE IF EXISTS ASSESMENT;
DROP TABLE IF EXISTS COLLEGES_APPLIED;
DROP TABLE IF EXISTS DEPENDENTS;
DROP TABLE IF EXISTS DOCUMENTS;
DROP TABLE IF EXISTS EDUCATION;
DROP TABLE IF EXISTS EMPLOYEE;
DROP TABLE IF EXISTS ENROLLMENT;
DROP TABLE IF EXISTS FRANCHISE;
DROP TABLE IF EXISTS IDENTITIY;
DROP TABLE IF EXISTS PAYMENTS;
DROP TABLE IF EXISTS PROJECT_LOOKUP;
DROP TABLE IF EXISTS WORK_EXPERIENCE;

CREATE TABLE APPLICANT (
  APPLICATION_ID        varchar(15) NOT NULL, 
  Application_Date      date NOT NULL, 
  First_Name            varchar(100) NOT NULL, 
  Last_Name             varchar(100) NOT NULL, 
  Date_Of_Birth         date NOT NULL, 
  Gender                char(1) NOT NULL, 
  Nationality           varchar(25) NOT NULL, 
  Father_Spouse_Name    varchar(100) NOT NULL, 
  Mother_Name           varchar(100) NOT NULL, 
  Marital_Status        varchar(30) NOT NULL, 
  Mobile_No             int(10) NOT NULL, 
  EMail                 varchar(100) NOT NULL, 
  Address               varchar(1000) NOT NULL, 
  City                  varchar(30) NOT NULL, 
  Village               varchar(30), 
  Mandal                varchar(30), 
  District              varchar(30) NOT NULL, 
  State                 varchar(30) NOT NULL, 
  Country               varchar(30) NOT NULL, 
  PinCode               int(10) NOT NULL, 
  Photo                 blob NOT NULL, 
  Referred_By           varchar(10) NOT NULL, 
  Application_Status    varchar(10) NOT NULL, 
  Created_By            int(10), 
  Application_Source_ID int(10));
CREATE TABLE ASSESMENT (
  APPLICATION_ID    varchar(15) NOT NULL, 
  ASSESSOR_ID       int(10) NOT NULL, 
  Assement_Date     date NOT NULL, 
  Assessment_Type   int(10) NOT NULL, 
  Status            varchar(20) NOT NULL, 
  Document_ID       varchar(30), 
  Image             blob NOT NULL, 
  Active            char(1) NOT NULL, 
  Comments          varchar(1000) NOT NULL, 
  Assessor_Comments varchar(1000) NOT NULL, 
  Assement_Type     int(10) NOT NULL, 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE COLLEGES_APPLIED (
  APPLICATION_ID     varchar(15) NOT NULL, 
  Course_Applied     varchar(100) NOT NULL, 
  Course_Group       varchar(50) NOT NULL, 
  Course_Branch      varchar(50) NOT NULL, 
  College_Applied    varchar(100) NOT NULL, 
  Board_University   varchar(100) NOT NULL, 
  Location           varchar(200) NOT NULL, 
  Application_Status varchar(20) NOT NULL, 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE DEPENDENTS (
  APPLICATION_ID       varchar(15) NOT NULL, 
  Dependent_ID         varchar(30) NOT NULL, 
  Dependent_Name       varchar(100) NOT NULL, 
  RELATIONSHIP_TYPE_ID varchar(20) NOT NULL, 
  Date_Of_Birth        date NOT NULL, 
  Country              int(10) NOT NULL, 
  Document_Image       blob NOT NULL, 
  Phone                int(15), 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE DOCUMENTS (
  DOCUMENT_SOURCE_ID           varchar(15) NOT NULL, 
  Document_Source              varchar(20) NOT NULL, 
  Document_File_Type           varchar(50) NOT NULL, 
  Document_Uploaded_Date       timestamp NOT NULL, 
  Document_File                blob NOT NULL, 
  Comments                     varchar(1000) NOT NULL, 
  Document_Uploaded_By         varchar(15), 
  Document_Verification_Status varchar(15), 
  Document_Verified_By         int(10), 
  DOCUMENT_ID                  varchar(20));
CREATE TABLE EDUCATION (
  APPLICATION_ID         varchar(15) NOT NULL, 
  Course_Name            varchar(100) NOT NULL, 
  Course_Group           varchar(50) NOT NULL, 
  Course_Branch          varchar(50) NOT NULL, 
  Course_Start_Date      date NOT NULL, 
  Course_Completion_Date date NOT NULL, 
  Percentage             decimal(5, 2) NOT NULL, 
  Institution            varchar(100) NOT NULL, 
  Board_University       varchar(100) NOT NULL, 
  Gap_Duration_Months    int(3), 
  Location               varchar(200) NOT NULL, 
  DOCUMENT_ID            varchar(20) NOT NULL, 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE EMPLOYEE (
  EMPLOYEE_ID  int(10) NOT NULL AUTO_INCREMENT, 
  FIRST_NAME   varchar(30) NOT NULL, 
  LAST_NAME    varchar(30) NOT NULL, 
  DATE_OF_JOIN date NOT NULL, 
  DEPARTMENT   varchar(10) NOT NULL, 
  DESIGNATION  varchar(100) NOT NULL, 
  PHONE_NO     int(15) NOT NULL, 
  EMAIL        varchar(255) NOT NULL, 
  USER_ID      varchar(10) NOT NULL, 
  PASSWORD     varchar(10) NOT NULL, 
  LAST_LOGIN   timestamp NOT NULL, 
  ACTIVE       varchar(10) NOT NULL, 
  AADHAAR_NO   int(20) NOT NULL, 
  ADDRESS      int(255) NOT NULL, 
  PHOTO        blob NOT NULL, 
  SALARY       decimal(10, 2) NOT NULL, 
  PF_NO        varchar(20) NOT NULL, 
  PAN_CARD     varchar(10) NOT NULL, 
  BRANCH_CODE  varchar(10) NOT NULL, 
  USER_TYPE    int(10) NOT NULL, 
  MANAGER_ID   int(10) NOT NULL, 
  PRIMARY KEY (EMPLOYEE_ID));
CREATE TABLE ENROLLMENT (
  APPLICATION_ID        varchar(15) NOT NULL, 
  TRAINING_ID           varchar(20) NOT NULL, 
  Training_Start_Date   date NOT NULL, 
  Training_End_Date     date NOT NULL, 
  Traning_Duration      int(10) NOT NULL, 
  Location              varchar(200) NOT NULL, 
  Training_Status_ID    int(10) NOT NULL, 
  Training_Time_Breakup varchar(10) NOT NULL, 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE FRANCHISE (
  FRANCHISE_ID         varchar(15) NOT NULL, 
  FRANCHISE_NAME       varchar(100) NOT NULL, 
  MANAGER_ID           int(10) NOT NULL, 
  FIRST_NAME           varchar(30) NOT NULL, 
  LAST_NAME            varchar(30) NOT NULL, 
  REGISTRATION_DATE    date NOT NULL, 
  PHONE_NO             int(15) NOT NULL, 
  ALTERNATE_CONTACT_NO int(10), 
  EMAIL                varchar(255) NOT NULL, 
  DESIGNATION          varchar(100) NOT NULL, 
  USER_ID              varchar(10) NOT NULL, 
  PASSWORD             varchar(10) NOT NULL, 
  LAST_LOGIN           timestamp NOT NULL, 
  ACTIVE               int(10) NOT NULL, 
  AADHAAR_NO           int(20) NOT NULL, 
  ADDRESS              int(255) NOT NULL, 
  PHOTO                blob NOT NULL, 
  DOCUMENT_ID          int(10) NOT NULL, 
  COMMISSION_AMOUNT    decimal(10, 2) NOT NULL, 
  PAN_CARD             varchar(10) NOT NULL, 
  GSTNO                varchar(30) NOT NULL, 
  CITY                 int(10) NOT NULL, 
  STATE                int(10) NOT NULL, 
  COUNTRY              int(10) NOT NULL, 
  PINCODE              int(10) NOT NULL, 
  Comments             varchar(1000) NOT NULL, 
  PRIMARY KEY (FRANCHISE_ID));
CREATE TABLE IDENTITIY (
  APPLICATION_ID      varchar(15) NOT NULL, 
  Proof_Of_Identity   varchar(20) NOT NULL, 
  ID_Number           varchar(20) NOT NULL, 
  Issued_Organization varchar(100) NOT NULL, 
  Start_Date          date NOT NULL, 
  End_Date            date NOT NULL, 
  Place_Of_ID_Issued  varchar(100) NOT NULL, 
  Country             int(10) NOT NULL, 
  Document_Image      blob NOT NULL, 
  PRIMARY KEY (APPLICATION_ID));
CREATE TABLE PAYMENTS (
  PAYMENT_DATE             date NOT NULL, 
  AMOUNT_PAID              decimal(12, 2) NOT NULL, 
  MODE_OF_PAYMENT          varchar(20) NOT NULL, 
  MODE_OF_PAYMENT_NO       varchar(30) NOT NULL, 
  PAYMENT_REFERENCE_NO     int(30) NOT NULL, 
  TRANSACTION_REFERENCE_NO varchar(20) NOT NULL, 
  SGST                     int(10) DEFAULT 0 NOT NULL, 
  IGST                     int(10) DEFAULT 0 NOT NULL, 
  GSTNO                    varchar(20) NOT NULL, 
  TRANSACTION_TYPE_ID      varchar(20) NOT NULL, 
  APPLICATION_ID           varchar(15) NOT NULL);
CREATE TABLE PROJECT_LOOKUP (
  LOOKUP_ID          varchar(20) NOT NULL, 
  LOOKUP_CODE        varchar(10) NOT NULL UNIQUE, 
  LOOKUP_TYPE        varchar(10) NOT NULL UNIQUE, 
  LOOKUP_CATEGORY    varchar(10) NOT NULL UNIQUE, 
  LOOKUP_NAME        varchar(10) NOT NULL, 
  LOOKUP_DESCRIPTION varchar(100) NOT NULL, 
  ACTIVE             char(1) NOT NULL, 
  PRIMARY KEY (LOOKUP_ID));
CREATE TABLE WORK_EXPERIENCE (
  APPLICATION_ID          varchar(15) NOT NULL, 
  Company_Name            varchar(100) NOT NULL, 
  INDUSTRY_CATEGORY_ID    varchar(20) NOT NULL, 
  Designation             varchar(50) NOT NULL, 
  Job_Description         varchar(1000) NOT NULL, 
  Total_Experience_Months int(10) NOT NULL, 
  Start_Date              date NOT NULL, 
  End_Date                date NOT NULL, 
  Location                varchar(100) NOT NULL, 
  Country                 int(30) NOT NULL, 
  PRIMARY KEY (APPLICATION_ID));

ALTER TABLE EDUCATION ADD CONSTRAINT FK_Applicant_Education FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE WORK_EXPERIENCE ADD CONSTRAINT FK_Applicant_WrkExperience FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE IDENTITIY ADD CONSTRAINT FK_Applicant_Identity FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE DEPENDENTS ADD CONSTRAINT FK_Applicant_Dependents FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE COLLEGES_APPLIED ADD CONSTRAINT FK_Applicant_Colleges_Applied FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE ENROLLMENT ADD CONSTRAINT FK_Applicant_Enrollment FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE DOCUMENTS ADD CONSTRAINT FK_Applicant_Documents FOREIGN KEY (DOCUMENT_SOURCE_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE PAYMENTS ADD CONSTRAINT FK_Applicant_Payments FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);
ALTER TABLE ASSESMENT ADD CONSTRAINT FK_Applicant_Assesment FOREIGN KEY (APPLICATION_ID) REFERENCES APPLICANT (APPLICATION_ID);

ALTER TABLE FRANCHISE ADD CONSTRAINT FK_Franchise_AdminEmp FOREIGN KEY (MANAGER_ID) REFERENCES EMPLOYEE (EMPLOYEE_ID);
ALTER TABLE ASSESMENT ADD CONSTRAINT FK_Assesment_Assessor FOREIGN KEY (ASSESSOR_ID) REFERENCES EMPLOYEE (EMPLOYEE_ID);
ALTER TABLE DOCUMENTS ADD CONSTRAINT FK_Franchise_DocumentSrc_LKP FOREIGN KEY (DOCUMENT_SOURCE_ID) REFERENCES FRANCHISE (FRANCHISE_ID);
ALTER TABLE ENROLLMENT ADD CONSTRAINT FK_Applicant_TrngEnrol_LKP FOREIGN KEY (TRAINING_ID) REFERENCES PROJECT_LOOKUP (LOOKUP_ID);
ALTER TABLE PAYMENTS ADD CONSTRAINT FK_Payments_TransTyp_LKP FOREIGN KEY (TRANSACTION_TYPE_ID) REFERENCES PROJECT_LOOKUP (LOOKUP_ID);
ALTER TABLE COLLEGES_APPLIED ADD CONSTRAINT FK_CollegesApplied_LKP FOREIGN KEY (Application_Status) REFERENCES PROJECT_LOOKUP (LOOKUP_ID);
ALTER TABLE IDENTITIY ADD CONSTRAINT FK_Identitiy_LKP FOREIGN KEY (Proof_Of_Identity) REFERENCES PROJECT_LOOKUP (LOOKUP_ID);
ALTER TABLE DEPENDENTS ADD CONSTRAINT FK_Dependents_LKP FOREIGN KEY (RELATIONSHIP_TYPE_ID) REFERENCES PROJECT_LOOKUP (LOOKUP_ID);
ALTER TABLE WORK_EXPERIENCE ADD CONSTRAINT FK_WorkExp_LKP FOREIGN KEY (INDUSTRY_CATEGORY_ID) REFERENCES PROJECT_LOOKUP (LOOKUP_ID);


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
  APPLICATION_ID = ?, 
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
  ;
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
  WHERE ;
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

