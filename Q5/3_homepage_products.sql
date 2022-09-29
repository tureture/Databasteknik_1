use ht22_1_project_group_14;
SELECT Prod_title, Description, Price, VAT, Discount
FROM Product
WHERE Prod_title IN ( SELECT HP_Prod_title
FROM HasProducts
WHERE HP_Dep_title="Homepage");
