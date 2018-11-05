# Challenge Set 9
## Part I: W3Schools SQL Lab 

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.

1. Which customers are from the UK?

   | ContactName       |
   | ----------------- |
   | Thomas Hardy      |
   | Victoria Ashworth |
   | Elizabeth Brown   |
   | Ann Devon         |
   | Helen Bennett     |
   | Simon Crowther    |
   | Hari Kumar        |


2. What is the name of the customer who has the most orders?

   | CustomerName | OrderCount |
   | ------------ | ---------- |
   | Ernst Handel | 10         |


3. Which supplier has the highest average product price?

   | SupplierName               | AvgProductPrice |
   | -------------------------- | --------------- |
   | Aux joyeux ecclésiastiques | 140.75          |

4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)

   | CountryCount |
   | ------------ |
   | 21           |

5. What category appears in the most orders?

   | CategoryName   | OrderCount |
   | -------------- | ---------- |
   | Dairy Products | 100        |


6. What was the total cost for each order?

   | TotalPrice  |
   | ----------- |
   | $386,424.23 |

   | OrderID | TotalPrice |
   | ------- | ---------- |
   | 10248   | 566        |
   | 10249   | 2329.25    |
   | 10250   | 2267.25    |
   | 10251   | 839.5      |
   | 10252   | 4662.5     |
   | 10253   | 1806       |
   | 10254   | 781.5      |
   | 10255   | 3115.75    |
   | 10256   | 648        |
   | 10257   | 1400.5     |
   | 10258   | 2529.75    |
   | 10259   | 126        |
   | 10260   | 2183.9     |
   | 10261   | 560        |
   | 10262   | 782.2      |
   | 10263   | 3086.4     |
   | 10264   | 906.25     |
   | 10265   | 1470       |
   | 10266   | 456        |
   | 10267   | 5040       |
   | 10268   | 1377.1     |
   | 10269   | 846        |
   | 10270   | 1720       |
   | 10271   | 60         |
   | 10272   | 1821.2     |
   | 10273   | 2679.5     |
   | 10274   | 673.6      |
   | 10275   | 384        |
   | 10276   | 525        |
   | 10277   | 1503.6     |
   | 10278   | 1862.4     |
   | 10279   | 585        |
   | 10280   | 766.5      |
   | 10281   | 108.2      |
   | 10282   | 194.34     |
   | 10283   | 1770       |
   | 10284   | 1816.95    |
   | 10285   | 2726.8     |
   | 10286   | 3772       |
   | 10287   | 1158       |
   | 10288   | 112        |
   | 10289   | 599.25     |
   | 10290   | 2713.85    |
   | 10291   | 692.8      |
   | 10292   | 1620       |
   | 10293   | 1061       |
   | 10294   | 2359.5     |
   | 10295   | 152        |
   | 10296   | 1315.5     |
   | 10297   | 1776       |
   | 10298   | 3909.5     |
   | 10299   | 438        |
   | 10300   | 760        |
   | 10301   | 944        |
   | 10302   | 3388.8     |
   | 10303   | 1555       |
   | 10304   | 1193       |
   | 10305   | 5197.25    |
   | 10306   | 624.15     |
   | 10307   | 530.5      |
   | 10308   | 111        |
   | 10309   | 2202.5     |
   | 10310   | 421        |
   | 10311   | 336        |
   | 10312   | 2019.9     |
   | 10313   | 228        |
   | 10314   | 2910       |
   | 10315   | 646        |
   | 10316   | 3547.5     |
   | 10317   | 360        |
   | 10318   | 301        |
   | 10319   | 1490.4     |
   | 10320   | 645        |
   | 10321   | 180        |
   | 10322   | 140        |
   | 10323   | 205.5      |
   | 10324   | 7698.45    |
   | 10325   | 1873.25    |
   | 10326   | 1227.5     |
   | 10327   | 2828.65    |
   | 10328   | 1462       |
   | 10329   | 6025.12    |
   | 10330   | 2431.5     |
   | 10331   | 111.75     |
   | 10332   | 2792       |
   | 10333   | 1192.5     |
   | 10334   | 181        |
   | 10335   | 3181.5     |
   | 10336   | 396        |
   | 10337   | 3087.52    |
   | 10338   | 1168.35    |
   | 10339   | 4330.4     |
   | 10340   | 3205.8     |
   | 10341   | 515        |
   | 10342   | 2876       |
   | 10343   | 1982.5     |
   | 10344   | 3570       |
   | 10345   | 3662       |
   | 10346   | 2164       |
   | 10347   | 1160.1     |
   | 10348   | 495        |
   | 10349   | 178.8      |
   | 10350   | 891.75     |
   | 10351   | 7103.6     |
   | 10352   | 194        |
   | 10353   | 13427      |
   | 10354   | 711.16     |
   | 10355   | 600        |
   | 10356   | 1383       |
   | 10357   | 1701.68    |
   | 10358   | 565        |
   | 10359   | 4572.2     |
   | 10360   | 9244.25    |
   | 10361   | 2842       |
   | 10362   | 1938.8     |
   | 10363   | 559        |
   | 10364   | 1187.5     |
   | 10365   | 504        |
   | 10366   | 170.25     |
   | 10367   | 1044.85    |
   | 10368   | 2294.05    |
   | 10369   | 3159.8     |
   | 10370   | 1467.5     |
   | 10371   | 114        |
   | 10372   | 15353.6    |
   | 10373   | 2135       |
   | 10374   | 573.75     |
   | 10375   | 423.25     |
   | 10376   | 525        |
   | 10377   | 1272       |
   | 10378   | 129        |
   | 10379   | 1200.6     |
   | 10380   | 1776.02    |
   | 10381   | 140        |
   | 10382   | 3628.76    |
   | 10383   | 1123.75    |
   | 10384   | 2778       |
   | 10385   | 1080       |
   | 10386   | 207.5      |
   | 10387   | 1323.6     |
   | 10388   | 1594.5     |
   | 10389   | 2292       |
   | 10390   | 2845.2     |
   | 10391   | 108        |
   | 10392   | 1800       |
   | 10393   | 4135.6     |
   | 10394   | 553        |
   | 10395   | 2920       |
   | 10396   | 2380.8     |
   | 10397   | 1054       |
   | 10398   | 3420       |
   | 10399   | 2207       |
   | 10400   | 3829.59    |
   | 10401   | 4837.02    |
   | 10402   | 3393.5     |
   | 10403   | 1258.95    |
   | 10404   | 2096.9     |
   | 10405   | 500        |
   | 10406   | 2527       |
   | 10407   | 1492.5     |
   | 10408   | 2030.2     |
   | 10409   | 399        |
   | 10410   | 1002.5     |
   | 10411   | 1514.25    |
   | 10412   | 465        |
   | 10413   | 2656       |
   | 10414   | 290.6      |
   | 10415   | 128        |
   | 10416   | 902        |
   | 10417   | 14104      |
   | 10418   | 2268.5     |
   | 10419   | 2760       |
   | 10420   | 2372       |
   | 10421   | 1595.7     |
   | 10422   | 62.46      |
   | 10423   | 1275       |
   | 10424   | 14366.5    |
   | 10425   | 600        |
   | 10426   | 422.75     |
   | 10427   | 813.75     |
   | 10428   | 240        |
   | 10429   | 2186.5     |
   | 10430   | 7245       |
   | 10431   | 3155       |
   | 10432   | 610.3      |
   | 10433   | 1064       |
   | 10434   | 450        |
   | 10435   | 790        |
   | 10436   | 2763.5     |
   | 10437   | 492        |
   | 10438   | 710.5      |
   | 10439   | 1348.7     |
   | 10440   | 7246.01    |
   | 10441   | 2195       |
   | 10442   | 2246       |
   | 10443   | 673.2      |


7. Which employee made the most sales (by total price)?

   | LastName | FirstName | EmployeeTotal |
   | -------- | --------- | ------------- |
   | Peacock  | Margaret  | 105696.5      |


8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)

   | EmployeeID | LastName  | FirstName | BirthDate  | Photo      | Notes                                                        |
   | ---------- | --------- | --------- | ---------- | ---------- | ------------------------------------------------------------ |
   | 3          | Leverling | Janet     | 1963-08-30 | EmpID3.pic | Janet has a BS degree in chemistry from Boston College). She has also completed a certificate program in food retailing management. Janet was hired as a sales associate and was promoted to sales representative. |
   | 5          | Buchanan  | Steven    | 1955-03-04 | EmpID5.pic | Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree. Upon joining the company as a sales representative, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London, where he was promoted to sales manager. Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management'. He is fluent in French. |

9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)

   | SupplierName  | AvgProductPrice | ProductCount |
   | ------------- | --------------- | ------------ |
   | Tokyo Traders | 46              | 3            |