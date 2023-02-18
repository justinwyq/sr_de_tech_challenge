CREATE TABLE memberships (
    membership_id varchar(50) PRIMARY KEY,
    application_id int NOT NULL,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    mobile_no int NOT NULL,
    date_of_birth date NOT NULL,
    above_18 bool NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL
);