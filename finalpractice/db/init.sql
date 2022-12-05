CREATE DATABASE IF NOT EXISTS myappdb;
use myappdb;

CREATE TABLE IF NOT EXISTS 'user' (  
  'name' varchar(50) NOT NULL,
  'lastname' varchar(100) NOT NULL,
  'role' varchar(100) NOT NULL
);

insert  into 'user'('name','lastname','role') values
('Ariana','Rodriguez','supervisor');