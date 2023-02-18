CREATE TABLE applications (
    application_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    date_of_birth VARCHAR(50) NOT NULL,
    mobile_no VARCHAR(50) NOT NULL
);