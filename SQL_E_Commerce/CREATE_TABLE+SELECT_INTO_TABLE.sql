DROP DATABASE IF EXISTS TestDB
CREATE DATABASE TestDB

DROP TABLE IF EXISTS marketing.customers
DROP SCHEMA IF EXISTS marketing

-- CREATE SCHEMA 
GO
CREATE SCHEMA marketing
GO

-- SELECT INTO
SELECT *
INTO marketing.customers
FROM BikeStores.sales.customers
GO

ALTER TABLE TestDB.marketing.customers ADD PRIMARY KEY(customer_id)

USE TestDB -- to use an existing database

DROP TABLE IF EXISTS sales.visits
DROP SCHEMA IF EXISTS sales

GO
CREATE SCHEMA sales
GO 

-- CREATE TABLE
CREATE TABLE sales.visits (
visit_id INT PRIMARY KEY IDENTITY(1, 1),
first_name VARCHAR(50) NOT NULL DEFAULT 0,
last_name VARCHAR(50) NOT NULL DEFAULT 0,
visited_at DATETIME DEFAULT GETDATE(),
exited_at DATETIME DEFAULT CURRENT_TIMESTAMP,
phone VARCHAR(50) NOT NULL DEFAULT 0,
customer_id INT NOT NULL DEFAULT 99,
FOREIGN KEY (customer_id) REFERENCES marketing.customers (customer_id))

-- INSERT INTO
INSERT INTO sales.visits (first_name)
VALUES ('Evren')

SELECT *
FROM sales.visits

 -- line comment
/* multi line
comment */

/* -char -- ne yazarsak yazalım belirlenen ölçüde hafızada yer tutar. 
   -varchar  -- bir karakter için 8kb yani 1byte yer tutar. char a nazaran hafızada kullanıldıgı kadar yer tutar. Ekonomiktir.
   -nvarchar -- varchar dan farkı bir karakter için 16kb yani 2byte yer tutar. Ozel karakter kullanimi için uygundur.
   +(özel bir koşul yok ise daima varchar kullanılmalı)
*/


/* Query Order
SELECT
    city,
    COUNT (*)
FROM
    sales.customers
WHERE
    state = 'CA'
GROUP BY
    city
HAVING
    COUNT (*) > 10
ORDER BY
    city;
*/

/* Identity olarak tanımladıgımız bir feature i manuel olarak degiştirmek istersek: 
use BikeStores;
SET IDENTITY_INSERT sales.visits ON;  
INSERT INTO sales.visits(visit_id,brand_name) VALUES(1,'Electra'),
INSERT INTO sales.visits(brand_id,brand_name) VALUES(2,'Haro')
INSERT INTO sales.visits(brand_id,brand_name) VALUES(3,'Redline')
SET IDENTITY_INSERT product.brand OFF; */