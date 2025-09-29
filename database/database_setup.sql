-- create the database
CREATE DATABASE momo_etl_dashboard;

-- select the database for use
USE momo_etl_dashboard;

-- create sms table
CREATE TABLE sms (
	sms_id BIGINT PRIMARY KEY,
	protocol VARCHAR(10),
	address VARCHAR(30),
	sms_date BIGINT, 
	readable_date VARCHAR(50), 
	body TEXT, 
	service_center VARCHAR(30),
	contact_name VARCHAR(50)
);

-- create category table
CREATE TABLE category ( 
	category_id INT PRIMARY KEY,
	category_name VARCHAR(50),
	description VARCHAR(255)
);

-- create transaction table
CREATE TABLE transaction (
	transaction_id BIGINT PRIMARY KEY,
	amount DECIMAL(18,2),
	currency VARCHAR(10),
	fee DECIMAL(18,2),
	balance_after DECIMAL(18,2),
	sms_id BIGINT, 
	category_id INT,
	FOREIGN KEY (sms_id) REFERENCES sms(sms_id), 
	raw_message TEXT, 
	FOREIGN KEY (category_id) REFERENCES category(category_id)
);

-- create user table
CREATE TABLE user(
    	user_id BIGINT PRIMARY KEY,
    	full_name VARCHAR(100),
    	phone_number VARCHAR(20),
    	account_number VARCHAR(30),
    	user_type VARCHAR(30)
);

-- create junction table between transaction and user
CREATE TABLE transaction_user (
	txn_user_id BIGINT PRIMARY KEY,
 	transaction_id BIGINT,
	user_id BIGINT,
	FOREIGN KEY (transaction_id) REFERENCES transaction(transaction_id),
	FOREIGN KEY (user_id) REFERENCES user(user_id) 
);

-- create systemlog table
CREATE TABLE SystemLog (
       	log_id BIGINT PRIMARY KEY, 
	transaction_id BIGINT NULL, 
	event_date DATETIME, 
	event_type VARCHAR(50), 
	message TEXT, 
	service_center VARCHAR(30), 
	FOREIGN KEY (transaction_id) REFERENCES transaction(transaction_id)
);


INSERT INTO sms (sms_id, protocol, address, sms_date, readable_date, body, service_center, contact_name) VALUES
(1,'SMS','+15550001',1695021000,'2025-09-18 09:30','Payment received','CenterA','Alice'),
(2,'SMS','+15550002',1695022000,'2025-09-18 09:45','Withdrawal successful','CenterB','Bob'),
(3,'SMS','+15550003',1695023000,'2025-09-18 10:00','Transfer completed','CenterC','Charlie'),
(4,'SMS','+15550004',1695024000,'2025-09-18 10:15','Deposit received','CenterD','Diana'),
(5,'SMS','+15550005',1695025000,'2025-09-18 10:30','Bill payment made','CenterE','Ethan');


INSERT INTO category (category_id, category_name, description) VALUES
(1,'Deposit','Money received into account'),
(2,'Withdrawal','Cash taken out'),
(3,'Transfer','Money sent to another account'),
(4,'Bill Payment','Utility or service payment'),
(5,'Fee','Charges or service fees');

INSERT INTO transaction (transaction_id, amount, currency, fee, balance_after, sms_id, category_id, raw_message) VALUES
(101,250.00,'USD',1.50,1250.00,1,1,'Payment received via mobile money'),
(102,100.00,'USD',0.50,1150.00,2,2,'ATM withdrawal'),
(103,75.00,'USD',0.25,1074.75,3,3,'Transfer to savings'),
(104,60.00,'USD',0.30,1014.45,4,4,'Electric bill payment'),
(105,10.00,'USD',0.10,1004.35,5,5,'Monthly service fee');

INSERT INTO user (user_id, full_name, phone_number, account_number, user_type) VALUES
(1,'Divine','+15550001','ACC1001','Customer'),
(2,'joy','+15550002','ACC1002','Customer'),
(3,'H.pucu','+15550003','ACC1003','Customer'),
(4,'Diana Prince','+15550004','ACC1004','Agent'),
(5,'Habib','+15550005','ACC1005','Customer');

INSERT INTO transaction_user (txn_user_id, transaction_id, user_id) VALUES
(1,101,1),
(2,102,2),
(3,103,3),
(4,104,4),
(5,105,5);

INSERT INTO SystemLog (log_id, transaction_id, event_date, event_type, message, service_center) VALUES
(1,101,'2025-09-18 11:00:00','INFO','Transaction 101 logged','CenterA'),
(2,102,'2025-09-18 11:05:00','INFO','Transaction 102 logged','CenterB'),
(3,103,'2025-09-18 11:10:00','WARNING','Delay in processing transaction 103','CenterC'),
(4,104,'2025-09-18 11:15:00','ERROR','Bill payment issue on transaction 104','CenterD'),
(5,105,'2025-09-18 11:20:00','DEBUG','Fee transaction 105 recorded','CenterE');

