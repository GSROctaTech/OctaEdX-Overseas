ALTER TABLE PAYMENTS DROP FOREIGN KEY FKPAYMENTS4632;
ALTER TABLE ORDERS_HEADER DROP FOREIGN KEY FKORDERS_HEA861715;
ALTER TABLE EMPLOYEE DROP FOREIGN KEY FKEMPLOYEE417948;
ALTER TABLE CUSTOMER DROP FOREIGN KEY FKCUSTOMER455232;
ALTER TABLE PRODUCT DROP FOREIGN KEY FKPRODUCT55849;
ALTER TABLE ORDER_DETAIL DROP FOREIGN KEY FKORDER_DETA63832;
ALTER TABLE ORDER_DETAIL DROP FOREIGN KEY FKORDER_DETA587440;
ALTER TABLE ORDERS_HEADER DROP FOREIGN KEY FKORDERS_HEA288647;
ALTER TABLE ORDERS_HEADER DROP FOREIGN KEY FKORDERS_HEA603597;
ALTER TABLE PAYMENTS DROP FOREIGN KEY FKPAYMENTS746513;
ALTER TABLE ORDERS_HEADER DROP FOREIGN KEY FKORDERS_HEA146157;
ALTER TABLE PAYMENTS DROP FOREIGN KEY FKPAYMENTS968349;
DROP TABLE IF EXISTS CUSTOMER;
DROP TABLE IF EXISTS EMPLOYEE;
DROP TABLE IF EXISTS ORDER_DETAIL;
DROP TABLE IF EXISTS ORDERS_HEADER;
DROP TABLE IF EXISTS PAYMENTS;
DROP TABLE IF EXISTS PRODUCT;
DROP TABLE IF EXISTS PROJECT_LOOKUP;
DROP TABLE IF EXISTS SUPPLIER;

CREATE TABLE CUSTOMER (
  CUSTOMER_ID           int(10) NOT NULL AUTO_INCREMENT, 
  FIRST_NAME            varchar(50) NOT NULL, 
  LAST_NAME             varchar(50) NOT NULL, 
  PHONE_NO              int(15) NOT NULL, 
  ADDRESS               varchar(255) NOT NULL, 
  CITY                  varchar(255) NOT NULL, 
  STATE                 varchar(255) NOT NULL, 
  COUNTRY               varchar(255) NOT NULL, 
  PIN_CODE              int(10) NOT NULL, 
  CREDIT_LIMIT          decimal(8, 2) NOT NULL, 
  CUSTOMER_TYPE         varchar(10) NOT NULL, 
  PAYMENT_DUE           decimal(12, 2) DEFAULT 0 NOT NULL, 
  MODE_OF_PAYMENT       varchar(30) NOT NULL, 
  PAYMENT_INSTRUMENT_NO int(30), 
  UPI_ID                varchar(30), 
  SALES_REP_ID          int(10) NOT NULL, 
  PRIMARY KEY (CUSTOMER_ID));
CREATE TABLE EMPLOYEE (
  EMPLOYEE_ID  int(10) NOT NULL AUTO_INCREMENT, 
  MANAGER      int(10) NOT NULL, 
  FIRST_NAME   varchar(30) NOT NULL, 
  LAST_NAME    varchar(30) NOT NULL, 
  DATE_OF_JOIN date NOT NULL, 
  PHONE_NO     int(15) NOT NULL, 
  EMAIL        varchar(255), 
  DESIGNATION  varchar(100) NOT NULL, 
  USER_ID      varchar(10) NOT NULL, 
  PASSWORD     varchar(10) NOT NULL, 
  LAST_LOGIN   timestamp(30) NOT NULL, 
  ACTIVE       int(10) NOT NULL, 
  AADHAAR_NO   int(20) NOT NULL, 
  ADDRESS      int(255), 
  PHOTO        blob, 
  SALARY       decimal(10, 2) NOT NULL, 
  PF_NO        varchar(20), 
  PAN_CARD     varchar(10), 
  PRIMARY KEY (EMPLOYEE_ID));
CREATE TABLE ORDER_DETAIL (
  ORDER_ID          int(10) NOT NULL UNIQUE, 
  ORDER_LINE_ID     int(10) NOT NULL UNIQUE, 
  PRODUCT_ID        int(10) NOT NULL, 
  QUANTITY          int(10) NOT NULL, 
  PRICE             decimal(10, 2) NOT NULL, 
  UOM               int(10) NOT NULL, 
  DISCOUNT          decimal(10, 2) NOT NULL, 
  LINE_TOTAL_AMOUNT decimal(10, 2) NOT NULL, 
  SGST              int(10) NOT NULL, 
  IGST              int(10) NOT NULL, 
  GSTNO             varchar(30) NOT NULL);
CREATE TABLE ORDERS_HEADER (
  ORDER_ID              int(10) NOT NULL AUTO_INCREMENT, 
  CUSTOMER_ID           int(10) NOT NULL, 
  ORDER_DATE            date NOT NULL, 
  DELIVERY_DATE         date NOT NULL, 
  SHIPPED_DATE          date NOT NULL, 
  ORDER_TOTAL_AMOUNT    decimal(12, 2) NOT NULL, 
  MODE_OF_PAYMENT       varchar(20) NOT NULL, 
  DOCUMENT_NO           varchar(30) NOT NULL comment 'Not null column, this column differentiates the type of transaction, column values will be either INVOICE_NO or PO_NUMBER', 
  USER_ID               int(10) NOT NULL, 
  COMMENTS              varchar(255) NOT NULL, 
  TRANSACTION_REF_NO    varchar(30) NOT NULL, 
  PAYMENT_GATEWAY       varchar(30) NOT NULL, 
  SUPPLIER_ID           int(10) NOT NULL, 
  TRANSACTION_TYPE_CODE varchar(10) NOT NULL comment 'Not null column, this column differentiates the type of transaction, column values will be either SALE or PURCHASE', 
  PRIMARY KEY (ORDER_ID));
CREATE TABLE PAYMENTS (
  CUSTOMER_ID              int(10) NOT NULL, 
  PAYMENT_DATE             date NOT NULL, 
  AMOUNT_PAID              decimal(12, 2) NOT NULL, 
  MODE_OF_PAYMENT          varchar(20) NOT NULL, 
  MODE_OF_PAYMENT_NO       varchar(30) NOT NULL, 
  PAYMENT_REFERENCE_NO     int(30) NOT NULL, 
  SUPPLIER_ID              int(10) NOT NULL, 
  TRANSACTION_TYPE_CODE    varchar(10) NOT NULL comment 'Not null column, this column differentiates the type of transaction, column values will be either AR(Accounts Receivable/Receipt i.e. Customer Payment) or AP(Account Payable/Payment i.e. Payment to Supplier)', 
  TRANSACTION_REFERENCE_NO varchar(20) NOT NULL, 
  SGST                     int(10) NOT NULL, 
  IGST                     int(10) NOT NULL, 
  GSTNO                    varchar(30) NOT NULL);
CREATE TABLE PRODUCT (
  PRODUCT_ID            int(10) NOT NULL AUTO_INCREMENT, 
  PRODUCT_NAME          varchar(255) NOT NULL UNIQUE, 
  PRODUCT_DESCRIPTION   varchar(255) NOT NULL, 
  UOM                   varchar(10) NOT NULL, 
  QUANTITY_IN_HAND      int(10) NOT NULL, 
  SUPPLIER_PRICE        decimal(12, 2) NOT NULL, 
  MSRP                  decimal(12, 2) NOT NULL, 
  ACTIVE                char(1) NOT NULL, 
  FSSAI_LICENSE_NUMBER  varchar(50), 
  PRODUCT_INTERNAL_CODE varchar(50), 
  PRODUCT_IMAGE         blob, 
  SUPPLIER_ID           int(10) NOT NULL, 
  PRIMARY KEY (PRODUCT_ID));
CREATE TABLE PROJECT_LOOKUP (
  LOOKUP_ID    varchar(15) NOT NULL UNIQUE, 
  LOOKUP_CODE  varchar(10) NOT NULL UNIQUE, 
  CATEGORY     int(10) NOT NULL UNIQUE, 
  SUB_CATEGORY int(10) NOT NULL UNIQUE, 
  DESCRIPTION  varchar(255) NOT NULL, 
  ACTIVE       char(1) NOT NULL, 
  IMAGE        blob);
CREATE TABLE SUPPLIER (
  SUPPLIER_ID     int(10) NOT NULL AUTO_INCREMENT, 
  FIRST_NAME      varchar(50) NOT NULL, 
  LAST_NAME       varchar(50) NOT NULL, 
  DESIGNATION     varchar(100) NOT NULL, 
  PHONE_NO        int(15) NOT NULL, 
  EMAIL           varchar(255) NOT NULL, 
  ADDRESS         varchar(255) NOT NULL, 
  USER_ID         varchar(10) NOT NULL, 
  PASSWORD        varchar(10) NOT NULL, 
  LAST_LOGIN      timestamp(30) NOT NULL, 
  ACTIVE          int(10) NOT NULL, 
  OD_LIMIT        decimal(10, 2) NOT NULL, 
  AMOUNT_DUE      int(12) NOT NULL, 
  BANK_NAME       int(100) NOT NULL, 
  BANK_LOCATION   varchar(255) NOT NULL, 
  BANK_ACCOUNT_NO varchar(30) NOT NULL, 
  IFSC_CODE       varchar(30) NOT NULL, 
  GSTNO           varchar(30) NOT NULL, 
  PRIMARY KEY (SUPPLIER_ID));
ALTER TABLE PAYMENTS ADD CONSTRAINT FKPAYMENTS4632 FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER (CUSTOMER_ID);
ALTER TABLE ORDERS_HEADER ADD CONSTRAINT FKORDERS_HEA861715 FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER (CUSTOMER_ID);
ALTER TABLE EMPLOYEE ADD CONSTRAINT FKEMPLOYEE417948 FOREIGN KEY (MANAGER) REFERENCES EMPLOYEE (EMPLOYEE_ID);
ALTER TABLE CUSTOMER ADD CONSTRAINT FKCUSTOMER455232 FOREIGN KEY (SALES_REP_ID) REFERENCES EMPLOYEE (EMPLOYEE_ID);
ALTER TABLE PRODUCT ADD CONSTRAINT FKPRODUCT55849 FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER (SUPPLIER_ID);
ALTER TABLE ORDER_DETAIL ADD CONSTRAINT FKORDER_DETA63832 FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCT (PRODUCT_ID);
ALTER TABLE ORDER_DETAIL ADD CONSTRAINT FKORDER_DETA587440 FOREIGN KEY (ORDER_ID) REFERENCES ORDERS_HEADER (ORDER_ID);
ALTER TABLE ORDERS_HEADER ADD CONSTRAINT FKORDERS_HEA288647 FOREIGN KEY (USER_ID) REFERENCES EMPLOYEE (EMPLOYEE_ID);
ALTER TABLE ORDERS_HEADER ADD CONSTRAINT FKORDERS_HEA603597 FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER (SUPPLIER_ID);
ALTER TABLE PAYMENTS ADD CONSTRAINT FKPAYMENTS746513 FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER (SUPPLIER_ID);
ALTER TABLE ORDERS_HEADER ADD CONSTRAINT FKORDERS_HEA146157 FOREIGN KEY (TRANSACTION_TYPE_CODE) REFERENCES PROJECT_LOOKUP (LOOKUP_CODE);
ALTER TABLE PAYMENTS ADD CONSTRAINT FKPAYMENTS968349 FOREIGN KEY (TRANSACTION_TYPE_CODE) REFERENCES PROJECT_LOOKUP (LOOKUP_CODE);

SELECT CUSTOMER_ID, FIRST_NAME, LAST_NAME, PHONE_NO, ADDRESS, CITY, STATE, COUNTRY, PIN_CODE, CREDIT_LIMIT, CUSTOMER_TYPE, PAYMENT_DUE, MODE_OF_PAYMENT, PAYMENT_INSTRUMENT_NO, UPI_ID, SALES_REP_ID 
  FROM CUSTOMER;
SELECT EMPLOYEE_ID, MANAGER, FIRST_NAME, LAST_NAME, DATE_OF_JOIN, PHONE_NO, EMAIL, DESIGNATION, USER_ID, PASSWORD, LAST_LOGIN, ACTIVE, AADHAAR_NO, ADDRESS, PHOTO, SALARY, PF_NO, PAN_CARD 
  FROM EMPLOYEE;
SELECT ORDER_ID, ORDER_LINE_ID, PRODUCT_ID, QUANTITY, PRICE, UOM, DISCOUNT, LINE_TOTAL_AMOUNT, SGST, IGST, GSTNO 
  FROM ORDER_DETAIL;
SELECT ORDER_ID, CUSTOMER_ID, ORDER_DATE, DELIVERY_DATE, SHIPPED_DATE, ORDER_TOTAL_AMOUNT, MODE_OF_PAYMENT, DOCUMENT_NO, USER_ID, COMMENTS, TRANSACTION_REF_NO, PAYMENT_GATEWAY, SUPPLIER_ID, TRANSACTION_TYPE_CODE 
  FROM ORDERS_HEADER;
SELECT CUSTOMER_ID, PAYMENT_DATE, AMOUNT_PAID, MODE_OF_PAYMENT, MODE_OF_PAYMENT_NO, PAYMENT_REFERENCE_NO, SUPPLIER_ID, TRANSACTION_TYPE_CODE, TRANSACTION_REFERENCE_NO, SGST, IGST, GSTNO 
  FROM PAYMENTS;
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_DESCRIPTION, UOM, QUANTITY_IN_HAND, SUPPLIER_PRICE, MSRP, ACTIVE, FSSAI_LICENSE_NUMBER, PRODUCT_INTERNAL_CODE, PRODUCT_IMAGE, SUPPLIER_ID 
  FROM PRODUCT;
SELECT LOOKUP_ID, LOOKUP_CODE, CATEGORY, SUB_CATEGORY, DESCRIPTION, ACTIVE, IMAGE 
  FROM PROJECT_LOOKUP;
SELECT SUPPLIER_ID, FIRST_NAME, LAST_NAME, DESIGNATION, PHONE_NO, EMAIL, ADDRESS, USER_ID, PASSWORD, LAST_LOGIN, ACTIVE, OD_LIMIT, AMOUNT_DUE, BANK_NAME, BANK_LOCATION, BANK_ACCOUNT_NO, IFSC_CODE, GSTNO 
  FROM SUPPLIER;

INSERT INTO CUSTOMER
  (CUSTOMER_ID, 
  FIRST_NAME, 
  LAST_NAME, 
  PHONE_NO, 
  ADDRESS, 
  CITY, 
  STATE, 
  COUNTRY, 
  PIN_CODE, 
  CREDIT_LIMIT, 
  CUSTOMER_TYPE, 
  PAYMENT_DUE, 
  MODE_OF_PAYMENT, 
  PAYMENT_INSTRUMENT_NO, 
  UPI_ID, 
  SALES_REP_ID) 
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
  ?);
INSERT INTO EMPLOYEE
  (EMPLOYEE_ID, 
  MANAGER, 
  FIRST_NAME, 
  LAST_NAME, 
  DATE_OF_JOIN, 
  PHONE_NO, 
  EMAIL, 
  DESIGNATION, 
  USER_ID, 
  PASSWORD, 
  LAST_LOGIN, 
  ACTIVE, 
  AADHAAR_NO, 
  ADDRESS, 
  PHOTO, 
  SALARY, 
  PF_NO, 
  PAN_CARD) 
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
  ?);
INSERT INTO ORDER_DETAIL
  (ORDER_ID, 
  ORDER_LINE_ID, 
  PRODUCT_ID, 
  QUANTITY, 
  PRICE, 
  UOM, 
  DISCOUNT, 
  LINE_TOTAL_AMOUNT, 
  SGST, 
  IGST, 
  GSTNO) 
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
INSERT INTO ORDERS_HEADER
  (ORDER_ID, 
  CUSTOMER_ID, 
  ORDER_DATE, 
  DELIVERY_DATE, 
  SHIPPED_DATE, 
  ORDER_TOTAL_AMOUNT, 
  MODE_OF_PAYMENT, 
  DOCUMENT_NO, 
  USER_ID, 
  COMMENTS, 
  TRANSACTION_REF_NO, 
  PAYMENT_GATEWAY, 
  SUPPLIER_ID, 
  TRANSACTION_TYPE_CODE) 
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
  ?);
INSERT INTO PAYMENTS
  (CUSTOMER_ID, 
  PAYMENT_DATE, 
  AMOUNT_PAID, 
  MODE_OF_PAYMENT, 
  MODE_OF_PAYMENT_NO, 
  PAYMENT_REFERENCE_NO, 
  SUPPLIER_ID, 
  TRANSACTION_TYPE_CODE, 
  TRANSACTION_REFERENCE_NO, 
  SGST, 
  IGST, 
  GSTNO) 
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
INSERT INTO PRODUCT
  (PRODUCT_ID, 
  PRODUCT_NAME, 
  PRODUCT_DESCRIPTION, 
  UOM, 
  QUANTITY_IN_HAND, 
  SUPPLIER_PRICE, 
  MSRP, 
  ACTIVE, 
  FSSAI_LICENSE_NUMBER, 
  PRODUCT_INTERNAL_CODE, 
  PRODUCT_IMAGE, 
  SUPPLIER_ID) 
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
INSERT INTO PROJECT_LOOKUP
  (LOOKUP_ID, 
  LOOKUP_CODE, 
  CATEGORY, 
  SUB_CATEGORY, 
  DESCRIPTION, 
  ACTIVE, 
  IMAGE) 
VALUES 
  (?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?, 
  ?);
INSERT INTO SUPPLIER
  (SUPPLIER_ID, 
  FIRST_NAME, 
  LAST_NAME, 
  DESIGNATION, 
  PHONE_NO, 
  EMAIL, 
  ADDRESS, 
  USER_ID, 
  PASSWORD, 
  LAST_LOGIN, 
  ACTIVE, 
  OD_LIMIT, 
  AMOUNT_DUE, 
  BANK_NAME, 
  BANK_LOCATION, 
  BANK_ACCOUNT_NO, 
  IFSC_CODE, 
  GSTNO) 
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
  ?);

UPDATE CUSTOMER SET 
  FIRST_NAME = ?, 
  LAST_NAME = ?, 
  PHONE_NO = ?, 
  ADDRESS = ?, 
  CITY = ?, 
  STATE = ?, 
  COUNTRY = ?, 
  PIN_CODE = ?, 
  CREDIT_LIMIT = ?, 
  CUSTOMER_TYPE = ?, 
  PAYMENT_DUE = ?, 
  MODE_OF_PAYMENT = ?, 
  PAYMENT_INSTRUMENT_NO = ?, 
  UPI_ID = ?, 
  SALES_REP_ID = ? 
WHERE
  CUSTOMER_ID = ?;
UPDATE EMPLOYEE SET 
  MANAGER = ?, 
  FIRST_NAME = ?, 
  LAST_NAME = ?, 
  DATE_OF_JOIN = ?, 
  PHONE_NO = ?, 
  EMAIL = ?, 
  DESIGNATION = ?, 
  USER_ID = ?, 
  PASSWORD = ?, 
  LAST_LOGIN = ?, 
  ACTIVE = ?, 
  AADHAAR_NO = ?, 
  ADDRESS = ?, 
  PHOTO = ?, 
  SALARY = ?, 
  PF_NO = ?, 
  PAN_CARD = ? 
WHERE
  EMPLOYEE_ID = ?;
UPDATE ORDER_DETAIL SET 
  ORDER_ID = ?, 
  ORDER_LINE_ID = ?, 
  PRODUCT_ID = ?, 
  QUANTITY = ?, 
  PRICE = ?, 
  UOM = ?, 
  DISCOUNT = ?, 
  LINE_TOTAL_AMOUNT = ?, 
  SGST = ?, 
  IGST = ?, 
  GSTNO = ? 
WHERE
  ;
UPDATE ORDERS_HEADER SET 
  CUSTOMER_ID = ?, 
  ORDER_DATE = ?, 
  DELIVERY_DATE = ?, 
  SHIPPED_DATE = ?, 
  ORDER_TOTAL_AMOUNT = ?, 
  MODE_OF_PAYMENT = ?, 
  DOCUMENT_NO = ?, 
  USER_ID = ?, 
  COMMENTS = ?, 
  TRANSACTION_REF_NO = ?, 
  PAYMENT_GATEWAY = ?, 
  SUPPLIER_ID = ?, 
  TRANSACTION_TYPE_CODE = ? 
WHERE
  ORDER_ID = ?;
UPDATE PAYMENTS SET 
  CUSTOMER_ID = ?, 
  PAYMENT_DATE = ?, 
  AMOUNT_PAID = ?, 
  MODE_OF_PAYMENT = ?, 
  MODE_OF_PAYMENT_NO = ?, 
  PAYMENT_REFERENCE_NO = ?, 
  SUPPLIER_ID = ?, 
  TRANSACTION_TYPE_CODE = ?, 
  TRANSACTION_REFERENCE_NO = ?, 
  SGST = ?, 
  IGST = ?, 
  GSTNO = ? 
WHERE
  ;
UPDATE PRODUCT SET 
  PRODUCT_NAME = ?, 
  PRODUCT_DESCRIPTION = ?, 
  UOM = ?, 
  QUANTITY_IN_HAND = ?, 
  SUPPLIER_PRICE = ?, 
  MSRP = ?, 
  ACTIVE = ?, 
  FSSAI_LICENSE_NUMBER = ?, 
  PRODUCT_INTERNAL_CODE = ?, 
  PRODUCT_IMAGE = ?, 
  SUPPLIER_ID = ? 
WHERE
  PRODUCT_ID = ?;
UPDATE PROJECT_LOOKUP SET 
  LOOKUP_ID = ?, 
  LOOKUP_CODE = ?, 
  CATEGORY = ?, 
  SUB_CATEGORY = ?, 
  DESCRIPTION = ?, 
  ACTIVE = ?, 
  IMAGE = ? 
WHERE
  ;
UPDATE SUPPLIER SET 
  FIRST_NAME = ?, 
  LAST_NAME = ?, 
  DESIGNATION = ?, 
  PHONE_NO = ?, 
  EMAIL = ?, 
  ADDRESS = ?, 
  USER_ID = ?, 
  PASSWORD = ?, 
  LAST_LOGIN = ?, 
  ACTIVE = ?, 
  OD_LIMIT = ?, 
  AMOUNT_DUE = ?, 
  BANK_NAME = ?, 
  BANK_LOCATION = ?, 
  BANK_ACCOUNT_NO = ?, 
  IFSC_CODE = ?, 
  GSTNO = ? 
WHERE
  SUPPLIER_ID = ?;

DELETE FROM CUSTOMER 
  WHERE CUSTOMER_ID = ?;
DELETE FROM EMPLOYEE 
  WHERE EMPLOYEE_ID = ?;
DELETE FROM ORDER_DETAIL 
  WHERE ;
DELETE FROM ORDERS_HEADER 
  WHERE ORDER_ID = ?;
DELETE FROM PAYMENTS 
  WHERE ;
DELETE FROM PRODUCT 
  WHERE PRODUCT_ID = ?;
DELETE FROM PROJECT_LOOKUP 
  WHERE ;
DELETE FROM SUPPLIER 
  WHERE SUPPLIER_ID = ?;