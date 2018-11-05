# Challenge Set 9
## Part I: W3Schools SQL Lab 

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.

1. Which customers are from the UK?

   SELECT CustomerName
   FROM Customers
   WHERE Country='UK'
   ;


2. What is the name of the customer who has the most orders?

   SELECT CustomerName, count(OrderID) as Count
   FROM
     (SELECT * 
     FROM Customers a 
     JOIN Orders b
     on a.CustomerID = b.CustomerID)
   GROUP BY CustomerName
   ORDER BY Count desc
   LIMIT 1

   ;


3. Which supplier has the highest average product price?

   SELECT SupplierName, AVG
   FROM
     (SELECT SupplierID, AVG(price) as AVG
     FROM [Products]
     GROUP BY SupplierID
     ORDER BY AVG desc
     LIMIT 1) a
   LEFT JOIN Suppliers b
   ON a.SupplierID = b.SupplierID

   ;

4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)

   SELECT COUNT (DISTINCT(Country)) as Country
   FROM [Customers]

   ;


5. What category appears in the most orders?

   SELECT CategoryName, Count
   FROM 
     (SELECT CategoryID, Count(CategoryID) as Count
     FROM [OrderDetails] a
     LEFT JOIN 
     Products B
     on a.ProductID = b.ProductID
     GROUP BY CategoryID
     ORDER BY Count desc
     LIMIT 1) a
   LEFT JOIN Categories b
   ON a.CategoryID = b.CategoryID

   ;


6. What was the total cost for each order?

   SELECT OrderID, sum(Price*Quantity) as Total_Cost
     FROM [OrderDetails] a
     LEFT JOIN 
     Products B
     on a.ProductID = b.ProductID
     GROUP BY OrderID

   ;


7. Which employee made the most sales (by total price)?

   SELECT FirstName, LastName, b.EmployeeID, Total_Cost
   FROM 
   (SELECT OrderID, sum(Price*Quantity) as Total_Cost
     FROM [OrderDetails] a
     LEFT JOIN 
     Products B
     on a.ProductID = b.ProductID
     GROUP BY OrderID
     ORDER BY Total_Cost desc 
     LIMIT 1) a
   LEFT JOIN ORDERS b
   on a.OrderID = b.OrderID
   LEFT JOIN Employees c
   on b.EmployeeID = c.EmployeeID;


8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)

   SELECT count(*) 
   FROM [Employees]
   WHERE Notes LIKE '%BS%'


9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)

   SELECT SupplierName, a.SupplierID, AVG
   FROM 
   (SELECT SupplierID, AVG(Price) as AVG
   FROM [Products]
   GROUP BY SupplierID
   HAVING COUNT(ProductID) > 2
   ORDER BY AVG desc
   LIMIT 1) a
   LEFT JOIN Suppliers b
   on a.SupplierID = b.SupplierID

