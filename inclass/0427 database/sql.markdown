SELECT LastName,FirstName FROM Employees Where BirthDate BETWEEN '1950-01-01' AND '1959-12-31';
SELECT ContactName,Address From Customers Where Country = 'USA';
SELECT ProductName From Products Where Price < 100;
SELECT ProductName From Products Where Price between 10 and 50;
SELECT * From Products Where Unit LIKE '%box%';


SELECT  * FROM Orders WHERE EmployeeID = 4 AND ShipperID = 3;
SELECT * FROM [Products] WHERE Price < 10 OR Price > 50;

SELECT ProductName FROM Products ORDER BY Price asc;
SELECT LastName,FirstName FROM [Employees] ORDER BY BirthDate desc;

SELECT City FROM Customers WHERE Country ='Germany' UNION SELECT City FROM Suppliers WHERE Country ='Germany';