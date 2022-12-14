use ht22_1_project_group_14;
select Prod_title, Description, Price, VAT, Discount, avg_rating
from ( SELECT Reviews.Prod_title, Description, Price, VAT, Discount, avg(Stars) as avg_rating
FROM Product
inner join Reviews on Reviews.Prod_title = Product.Prod_title
Group by Prod_title ) as T1
where Prod_title in (select HP_Prod_title from HasProducts where HP_Dep_title="Pets"); 
