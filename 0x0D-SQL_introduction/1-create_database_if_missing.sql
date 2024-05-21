-- creating a database
-- oh i know how to do it!
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'hbtn_0c_0')
BEGIN
    CREATE database hbtn_0c_0;
END
ELSE
BEGIN
    PRINT 'DATABASE ALREADY EXISTS'
END