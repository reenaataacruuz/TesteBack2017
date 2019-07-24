desafio.py
import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=Desafio1;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM tb_customer_account")
for row in cursor:
    print('row = %r' % (row,))

Banco de dados:
CREATE DATABASE Desafio1

USE Desafio1

CREATE TABLE tb_customer_account (id_customer INT, cpf_cnpj NVARCHAR(13), nm_customer NVARCHAR(50), 
                                      is_active CHAR(1), vl_total INT)

INSERT INTO tb_customer_account VALUES (1500, '1112223345', 'Amanda', 'V', 500); 
INSERT INTO tb_customer_account VALUES (1600, '1112223346', 'Bruno', 'V', 510); 
INSERT INTO tb_customer_account VALUES (1700, '1112223347', 'Carla', 'V', 520); 
INSERT INTO tb_customer_account VALUES (1800, '1112223348', 'Dario', 'V', 530); 
INSERT INTO tb_customer_account VALUES (1900, '1112223349', 'Ellen', 'V', 530); 
INSERT INTO tb_customer_account VALUES (2000, '1112223340', 'Flavio', 'V', 540); 
INSERT INTO tb_customer_account VALUES (2100, '1112223351', 'Geogia', 'V', 550); 
INSERT INTO tb_customer_account VALUES (2200, '1112223352', 'Hilda', 'V', 560); 
INSERT INTO tb_customer_account VALUES (2300, '1112223353', 'Amelio', 'V', 570); 
INSERT INTO tb_customer_account VALUES (2400, '1112223354', 'Bianca', 'V', 580); 
INSERT INTO tb_customer_account VALUES (2500, '1112223355', 'Carlos', 'V', 590); 
INSERT INTO tb_customer_account VALUES (2600, '1112223356', 'Dalla', 'V', 600); 
INSERT INTO tb_customer_account VALUES (2700, '1112223357', 'Elton', 'V', 610); 
INSERT INTO tb_customer_account VALUES (2800, '1112223358', 'Flavia', 'V', 620);

SELECT id_customer, AVG(vl_total) as 'Media do VT'FROM tb_customer_account 
WHERE vl_total >=560 AND id_customer BETWEEN 1500 AND 2700  ORDER BY desc


GO
